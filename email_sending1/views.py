from django.shortcuts import render
from django.http import HttpResponse

from .tasks import send_email_task

# this function is responsible to run the task
def index(request):
    """here it call "send_email_task function when it will success it will return in the main page EMAIL HAS BEEN SENT WITH CELERY! """
    send_email_task()
    return HttpResponse('<h1>EMAIL HAS BEEN SENT WITH CELERY!</h1>')
