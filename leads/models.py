from django.db import models
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL

class Lead(models.Model):

    STATUS_CHOICES = {
        ('NEW','New'),
        ('CONTACTED', 'Contacted'),
        ('QUALIFIED','Qualified'),
        ('CONVERTED','Converted'),
    }

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    source = models.CharField(blank=True,null=True, max_length=100)
    status = models.CharField(choices=STATUS_CHOICES,default="NEW", max_length=20)
    assigned_to = models.ForeignKey(User, null=True,related_name="leads", on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, related_name='created_leads', on_delete=models.CASCADE)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name