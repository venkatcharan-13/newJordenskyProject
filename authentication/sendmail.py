from email import message
from lib2to3.pgen2 import token
from django.core.mail import send_mail

from django.conf import settings

def sendForgetPasswordLink(email,token):
    
    subject='Forgot Password Link'
    message=f'Hi there! here is your forgot password link to reset you password click on that http://127.0.0.1:8000/auth/changepassword/{token}'
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message,email_from,recipient_list)
    return True