from rest_framework import serializers
from .models import MasterList, Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'completed', 'created_at']


class MasterListSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True, read_only=True)

    class Meta:
        model = MasterList
        fields = ['id', 'name', 'description', 'created_at', 'todos']
