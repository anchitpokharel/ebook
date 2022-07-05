from django.db import models

# Create your models here.    
class contact_us(models.Model):
    
    your_name = models.CharField(max_length=255)
    your_number = models.CharField(max_length=255)
    your_email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=255)
    