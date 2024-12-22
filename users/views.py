from .models import User
from rest_framework import status
from .serializers import UserSerializers
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response






class UserRegView(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        serial=UserSerializers(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response({'message': 'User was created succesfuly'}, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        