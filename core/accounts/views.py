from django.shortcuts import render
from .tasks import sendMail
from django.http import HttpResponse 
# Create your views here.

def send_email(request):
    sendMail.delay()
    return HttpResponse('sent sucessfully')