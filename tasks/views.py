from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task
from .permissions import IsAdminOrManager
# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class= TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        
        if user.role in ['ADMIN','MANAGER']:
            return Task.objects.all()
        return Task.objects.select_related('customer','lead','assigned_to').filter(assigned_to=user)
    
    def perform_create(self, serializer):
        return serializer.save(created_by= self.request.user)
    
    def get_permissions(self):
        if self.action in ['create','update','partial_update','destroy']:
            return [IsAuthenticated(),IsAdminOrManager()]
        return [IsAuthenticated()]