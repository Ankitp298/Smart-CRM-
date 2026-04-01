from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields= [
                'id', 'title', 'description', 'task_type',
                'status', 'due_date', 'assigned_to',
                'lead', 'customer', 'created_at'
            ]
        read_only_fields = ["creaed_by","created_at"]