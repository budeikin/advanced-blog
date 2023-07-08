from django.shortcuts import render
from .tasks import sendMail
from django.http import HttpResponse,JsonResponse
import requests
from django.views.decorators.cache import cache_page
from django.core.cache import cache
# Create your views here.

def send_email(request):
    sendMail.delay()
    return HttpResponse('sent sucessfully')

@cache_page(60)
def test(request):
    response = requests.get('https://ce001c70-2433-4dd9-97d8-49c3c83af911.mock.pstmn.io/test/delay/5/')
    return JsonResponse(response.json())