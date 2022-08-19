from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from fetchTransaction import *
from authentication.models import *

from Jordensky.widgets import *

admin.site.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    formfield_overrides= {
        models.DateField:{'widget':PastCustomDatePickerWidget}
    }

# class MyModelAdmin(admin.ModelAdmin):
#     def get_urls(self):
#         urls = super().get_urls()
#         my_urls = [
#             path('create/user', self.admin_site.admin_view(self.my_view)),
#         ]
#         print(my_urls)
#         return my_urls + urls

#     def my_view(self, request):
#         users=get_user_model()
#         context={'allUsersList':users.objects.all()}
#         return TemplateResponse(request,'createUser.html',context)