from django.contrib.auth.models import User
from .models import Task
from rest_framework import viewsets
from .serializers import UserSerializer, TaskSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny



class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class TaskViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        if self.action == "destroy":
            return [IsAuthenticated()]
        else:
            return [AllowAny()]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    