from django.contrib.auth.models import User
from .models import Task
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password", "is_superuser"]
        
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        
    def get_queryset(self):
        return Task.objects.select_related("user").all()