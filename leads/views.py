from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Lead
from .serializers import LeadSerializer
from .permissions import IsAdminOrManager
from customers.models import Customer

# Create your views here.

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = LeadSerializer

    def get_queryset(self):
        user = self.request.user
        print("USER ROLE:", user.role)

        if user.role == 'ADMIN':
            return Lead.objects.all()
        return Lead.objects.select_related('assigned_to','created_by').filter(assigned_to=user)
    
    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)

    def get_permissions(self):
        if self.action in ['create','update','partial_update','destroy']:
            return [IsAuthenticated(),IsAdminOrManager()]
        return [IsAuthenticated()]
    
    # CONVERT Lead to CUSTOMER
    @action(detail=True, methods=["POST"])
    def convert(self , request, pk = None):
        lead = self.get_object()

        if lead.status == "CONVERTED":
            return Response({"message":"Already Converted !!"})
        
        # Create Customer
        customer = Customer.objects.create(
            name = lead.name,
            email = lead.email,
            phone = lead.phone,
            created_by = request.user,
        )

        lead.status = 'CONVERTED'
        lead.save()
        return Response({
            "message": "Lead converted to Customer",
            "customer_id": customer.id
        })