from django import views
from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('user/add',views.createUser,name='create user'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('createuser',views.createUser,name='Creating New User'),
    path('savenewUser',views.saveNewUser,name='saving new user'),
    path('fetchapis',views.fetchApis,name='Fetch Apis'),
    path('fetchapiTotal',views.fetchApisEndpoint,name='saving transactions'),
    path('forgetpassword',views.forgetPassword,name='forgot password'),
    path('changepassword/<token>',views.changePassword,name='change password')
    
]
