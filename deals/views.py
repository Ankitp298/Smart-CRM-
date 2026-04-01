from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Deal
from .serializers import DealSerializer
from .permissions import IsAdminOrManager
# Create your views here.

class DealViewSet(viewsets.ModelViewSet):
    queryset = Deal.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = DealSerializer

    def get_queryset(self):
        user = self.request.user

        if user.role == 'ADMIN':
            return Deal.objects.all()
        return Deal.objects.select_related('assigned_to','customer').filter(assigned_to = user)
    
    def perform_create(self, serializer):
        return serializer.save(created_by = self.request.user)
    
    def get_permissions(self):
        if self.action in ['create','update','partial_update','destroy']:
            return [IsAuthenticated(),IsAdminOrManager()]
        return [IsAuthenticated()]