from rest_framework import serializers
from .models import Lead

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = [
                    'id', 'name', 'email', 'phone',
                    'source', 'status', 'assigned_to',
                    'created_at']
        read_only_fields = ['created_at', 'created_by']

    def validate_assigned_to(self, value):
        if value.role != 'EXECUTIVE':
            raise serializers.ValidationError("Leads must be assigned to executives")
        return value