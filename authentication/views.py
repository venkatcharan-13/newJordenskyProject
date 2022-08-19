from distutils.log import error
import email
import profile
import re
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.contrib import messages
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Profile

from fetchTransaction import *
from .sendmail import sendForgetPasswordLink
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, ("Invalid credentials! Please enter correct username and password"))
            return redirect(login_view)
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully")
    return render(request, 'registration/logout.html')



# Forget Password 
def changePassword(request,token):
    context={}
    try:
        profile_obj=Profile.objects.filter(forget_password_token=token).first()
        print(profile_obj.user.id)
        context={'user_id': profile_obj.user.id}

        if request.method=='POST':
            new_password= request.POST.get('new_password')
            confirm_password=request.POST.get('confirm_password')
            user_id=request.POST.get('user_id')
            if user_id is None:
                messages.success(request,'No User is Fount')
                return redirect(changePassword)
            
            if new_password!=confirm_password:
                messages.success(request,'both should be equal ')
                return redirect(changePassword)

            user_obj=User.objects.get(id= user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect(login_view)

        
    except Exception as error:
        print(error)
    
    return render(request,'chagnePassword.html',context)

import uuid
def forgetPassword(request):
    try:
        if request.method=='POST':
            userName=request.POST.get('username')
            if not User.objects.filter(username=userName).first():
                messages.success(request,'No user found with this user name')
                return redirect(forgetPassword)
        
            user_obj=User.objects.get(username=userName)

            token=str(uuid.uuid4())
            # profile_obj=Profile.objects.get(user=user_obj)
            # profile_obj.forget_password_token=token
            # profile_obj.save()
            sendForgetPasswordLink(user_obj.email,token)
            messages.success(request,'Link Sent to Email Successfully')
            return redirect(login_view)       

    except Exception as error:
        print(error)
    return render(request,'forgetpassword.html')







def createUser(request):

    users=get_user_model()
    context={'allUsersList':users.objects.all()}

    return render(request,'createUser.html',context)

@csrf_exempt
def saveNewUser(request):

    User = get_user_model()
    request_body=json.loads(request.body)
    userEmail=request_body['userEmail']
    userPassword=request_body['userPassword']
    userUserName=request_body['userUsername']
    IsStaff=request_body['isStaff']
    user = User.objects.create_user(username=userUserName,email=userEmail,password=userPassword)
    user.is_superuser = False
    user.is_staff = IsStaff
    user.save()

    return JsonResponse({'Message': 'Success'})


def fetchApis(request):
    return render(request,'fetchTransactionsdetails.html')
@csrf_exempt
def fetchApisEndpoint(request):

    request_body=json.loads(request.body)
    organisation_id=request_body['userOrganisationId']
    UserName=request_body['userName']
    users=get_user_model()
    user_id=users.objects.filter(username=UserName).all()
    fetchingCompleteDetails(organisation_id,user_id[0].id)
    
    return JsonResponse({'Message':"Success"})
