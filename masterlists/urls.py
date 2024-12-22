from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from .views import MasterListViewSet, TodoViewSet

# Main router for master lists
router = DefaultRouter()
router.register('masterlists', MasterListViewSet, basename='masterlist')

# Nested router for todos within a master list
nested_router = NestedSimpleRouter(router, 'masterlists', lookup='master_list')
nested_router.register('todos', TodoViewSet, basename='todo')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
]
