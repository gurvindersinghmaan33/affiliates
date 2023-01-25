from django.db import models
from rest_framework import serializers
# Create your models here.
class Deal(models.Model):
    logo = models.CharField(max_length=300)
    label = models.CharField(max_length=300)
    image = models.CharField(max_length=300)
    price_text = models.CharField(max_length=300)
    price_main = models.CharField(max_length=300)
    profit_link = models.CharField(max_length=300)    

    def __str__(self):
         return self.price_main

class Contact(models.Model):
    firstName = models.CharField(max_length=100, blank=False)
    lastName = models.CharField(max_length=100 , blank=False)
    email = models.EmailField(max_length=100, blank=False)
    phone = models.CharField(max_length=100, blank=False)
    message = models.CharField(max_length=1000, blank=False)
    def __str__(self):
         return f"Message from {self.firstName}"

class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields ="__all__"