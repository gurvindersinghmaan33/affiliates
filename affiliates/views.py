from django.shortcuts import render
from data.models import DealSerializer, Deal, Contact
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from django.contrib import messages

def index(request):
    data = Deal.objects.all()
    return render(request, 'index.html', {'products':data})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method=='POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        print(firstName, lastName, email, phone, message)
        if(len(firstName.strip()) >= 3 and len(email.strip()) >= 8 and len(phone.strip()) >= 10 and len(phone.strip()) <= 13 and len(message.strip()) != 0):
            Contact(firstName=firstName, lastName=lastName, email=email, phone=phone, message=message).save()
            messages.success(request, 'Your message has been received. Thanks for reaching to us. We will get back to you shortly😊.')
        else:
            messages.error(request, 'Fields marked with * are mandetory.')
    return render(request, 'contact.html')

@api_view(['POST'])
def api(request):
    if request.method=='POST':
        dealSerializer = DealSerializer(data=request.data)
        if dealSerializer.is_valid():
            dealSerializer.save()
            return Response({'message': 'Saved Succesfully'} , status=status.HTTP_201_CREATED)
        return Response(dealSerializer.errors)