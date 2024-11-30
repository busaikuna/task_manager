from django.db import models
from django.contrib.auth.models import User


STATUS = [("pendente", "pendente"), ("em andamento", "em andamento"), ("concluido", "concluido")]

class Task(models.Model):
    user_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    status = models.CharField(choices=STATUS, default="pendente", max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title