from django.db import models

STATUS = [("pendente", "pendente"), ("em andamento", "em andamento"), ("concluido", "concluido")]

class Task():
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    status = models.CharField(choices=STATUS, default="pendente")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title