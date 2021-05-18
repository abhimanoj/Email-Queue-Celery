from celery import shared_task

from django.core.mail import send_mail

from time import sleep

from mailqueue.models import MailerMessage
# Create your views here.


# Create mail message fuction 

def create_mail_message():
    """Here gives email subject , to_address email id , from_address email id , content of messaage , html_contennt of message"""
    new_message = MailerMessage()
    new_message.subject = "My Subject" 
    new_message.to_address = "jarnail@saavi.com.au"
    new_message.from_address = "dhirendra@saavi.com.au"
    new_message.content = "Mail content"
    new_message.html_content = "<h1>Mail Content</h1>"
    new_message.app = "this is test email please ignore."
    new_message.save()


@shared_task
def send_email_task():
    """call create_mail_message function it returns true"""
    create_mail_message()

    return True
