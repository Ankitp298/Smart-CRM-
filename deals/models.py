from django.db import models
from django.conf import settings
from customers.models import Customer
from django.core.validators import MinValueValidator
# Create your models here.
User = settings.AUTH_USER_MODEL

class Deal(models.Model):
    STAGE_CHOICES =(
        ('NEW','New'),
        ('NEGOTIATION','Negotiation'),
        ('WON','Won'),
        ('LOST','Lost'),
    )

    title = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, related_name='deals', on_delete=models.CASCADE)
    value =  models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0)])
    stage = models.CharField(max_length=20,choices=STAGE_CHOICES,default='NEW')
    expected_close_date = models.DateField(null= True ,blank= True)
    assigned_to = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, related_name='created_deals', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    