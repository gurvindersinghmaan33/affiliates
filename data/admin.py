from django.contrib import admin

# Register your models here.
from .models import Deal, Contact
   
admin.site.register(Deal)
admin.site.register(Contact)