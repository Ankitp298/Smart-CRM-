from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.db.models import Sum
from customers.models import Customer
from leads.models import Lead
from deals.models import Deal
# Create your views here.

class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
         # 💰 Total Revenue (only WON deals)
        total_revenue = Deal.objects.filter(stage="WON").aggregate(
            total= Sum("value")
        )['total'] or 0

        # 📊 Deals Stats
        total_deals = Deal.objects.count()
        won_deals = Deal.objects.filter(stage = 'WON').count()
        lost_deals = Deal.objects.filter(stage="LOST").count()

        # 🎯 Lead Conversion Rate
        total_leads = Lead.objects.count()
        converted_leads = Lead.objects.filter(status='CONVERTED').count()

        converted_leads = 0
        if total_leads > 0:
            conversion_rate = (converted_leads / total_leads) * 100

        total_customers = Customer.objects.count()

        return Response({
            "total_revenue":total_revenue,
            "total_deal":total_deals,
            "won_deal": won_deals,
            "lost_deal":lost_deals,
            'total_lead':total_leads,
            "conversion_rate":round(conversion_rate,2),
            "total_customer":total_customers
        })