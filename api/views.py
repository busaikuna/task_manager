from django.contrib.auth.models import User
from .models import Task
from rest_framework import viewsets
from .serializers import UserSerializer, TaskSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination


class TaskPagination(PageNumberPagination):
    page_size = 10


class UserPagination(PageNumberPagination):
    page_size = 10


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    pagination_class = UserPagination
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    pagination_class = TaskPagination
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["title", "created_at"]
    ordering = ["created_at", "title"]
    filterset_fields = ["status"]
    
    def get_queryset(self):
        return Task.objects.filter(user_owner = self.request.user)
       
       
class ListUserTasks(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = TaskPagination
    
    def get(self, request, pk):
        user = User.objects.get(pk = pk)
        if user == None:
            return Response(status=404)
        if user != request.user:
            return Response(status=403)
        tasks = Task.objects.filter(user_owner = user)
        serializer = TaskSerializer(tasks, many=True, context = {
            "request": request
        })
        
        return Response(serializer.data)