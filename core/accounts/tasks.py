from celery import shared_task
from time import sleep


@shared_task
def sendMail():
    sleep(3)
    print('sent successfully')