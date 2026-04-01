from rest_framework import serializers
from .models import Deal

class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = ['id', 'title', 'customer', 'value',
                    'stage', 'expected_close_date',
                    'assigned_to', 'created_at'
                    ]
        read_only_fields = ['created_by','created_at']
