from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import MasterList, Todo
from .serializers import MasterListSerializer, TodoSerializer


class MasterListViewSet(ModelViewSet):
    queryset = MasterList.objects.all()
    serializer_class = MasterListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return master lists for the logged-in user
        return MasterList.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically associate the master list with the logged-in user
        serializer.save(user=self.request.user)


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['completed']  # Enable filtering by 'completed'
    search_fields = ['title', 'description']  # Allow searching by title or description
    ordering_fields = ['created_at']  # Allow ordering by creation date

    def get_queryset(self):
        # Filter todos by the specified master list and logged-in user
        master_list_id = self.kwargs['master_list_pk']
        return Todo.objects.filter(master_list__id=master_list_id, master_list__user=self.request.user)

    def perform_create(self, serializer):
        # Associate the todo with its master list
        master_list_id = self.kwargs['master_list_pk']
        master_list = MasterList.objects.get(id=master_list_id, user=self.request.user)
        serializer.save(master_list=master_list)
