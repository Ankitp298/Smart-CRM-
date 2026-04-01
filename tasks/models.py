from django.db import models
from django.conf import settings
from leads.models import Lead
from customers.models import Customer
# Create your models here.
User = settings.AUTH_USER_MODEL

class Task(models.Model):
    TASK_TYPE_CHOICES = (
        ('CALL','Call'),
        ('MEETING','Meeting'),
        ('FOLLOW_UP','Follow Up'),
    )

    STATUS_CHOICES = (
        ('PENDING','Pending'),
        ('COMPLETED','Completed'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(null= True , blank=True)
    task_type= models.CharField(max_length=20, choices=TASK_TYPE_CHOICES)
    status = models.CharField( max_length=20,choices=STATUS_CHOICES,default='PEDNING')
    due_date = models.DateTimeField()
    assigned_to = models.ForeignKey(User,related_name='tasks',null=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, related_name='created_tasks', on_delete=models.CASCADE)
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateField( auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title