from django.urls import path
from reports import views

urlpatterns = [
    path('dashboard/',views.DashboardView.as_view(),name='dashboard'),
]
