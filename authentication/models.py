from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    forget_password_token=models.CharField(max_length=100,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    datepicker=models.DateField(default=datetime.date.today())

    def __str__(self):
        return self.user.username