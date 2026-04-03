from celery import shared_task
from django.core.mail import send_mail
import os

def send_task_reminder(email, task_title):
    send_mail(
        subject="Task Reminder",
        message=f'Reminder: {task_title}',
        from_email= os.getenv('EMAIL_USER'),
        recipient_list= [email],
    )