from django.contrib import admin
from .models import Deal

# Register your models here.
@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('title', 'customer', 'value', 'stage', 'assigned_to')
    list_filter = ('stage',)