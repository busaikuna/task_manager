from django.contrib.auth.models import User
from .models import Task
from rest_framework import viewsets
from .serializers import UserSerializer, TaskSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


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
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["title", "created_at"]
    ordering = ["created_at", "title"]
    filterset_fields = ["status"]
       
class ListUserTasks(APIView):
    def get(self, request, pk):
        user = User.objects.get(pk = pk)
        if user == None:
            return Response(status=404)
        tasks = Task.objects.filter(user_owner = user)
        serializer = TaskSerializer(tasks, many=True, context = {
            "request": request
        })
        return Response(serializer.data)