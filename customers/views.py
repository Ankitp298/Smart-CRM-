from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Customer
from .permissions import IsAdminOrManager,IsOwnerOrAdmin
from .serializers import CustomerSerializer
# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == "ADMIN":
            return Customer.objects.all()
        return Customer.objects.select_related('created_by').filter(created_by = user)

    def perform_create(self, serializer):
        serializer.save(created_by =self.request.user)

    def get_permissions(self):
        if self.action in ['create','update','partial_update','detroy']:
            return [IsAuthenticated(),IsAdminOrManager()]
        return [IsAuthenticated()]