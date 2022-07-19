from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    entity_name = models.CharField(max_length=100)
    industry_name = models.CharField(max_length=100)
    contact_number = PhoneNumberField()
    company_email = models.CharField(max_length=30, null=True)
    gst_number = models.CharField(max_length=20)
    pan_number = models.CharField(max_length=20)
    pf_number = models.CharField(max_length=20, null=True)
    esic_number = models.CharField(max_length=20, null=True)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class CompanyAddress(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    address_line = models.TextField()
    locality = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    pin_code = models.CharField(max_length=6)


class CompanyContext(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    about = models.TextField(blank=True, null=True)
    work_profile = models.TextField(blank=True, null=True)
    key_info = models.TextField(blank=True, null=True)
    specific_request = models.TextField(blank=True, null=True)


class BankDetail(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=15)
    ifsc_code = models.CharField(max_length=15)
    location = models.CharField(max_length=50)