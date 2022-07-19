# Generated by Django 4.0.5 on 2022-07-19 07:31

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('entity_name', models.CharField(max_length=100)),
                ('industry_name', models.CharField(max_length=100)),
                ('contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('company_email', models.CharField(max_length=30, null=True)),
                ('gst_number', models.CharField(max_length=20)),
                ('pan_number', models.CharField(max_length=20)),
                ('pf_number', models.CharField(max_length=20, null=True)),
                ('esic_number', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyContext',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(blank=True, null=True)),
                ('work_profile', models.TextField(blank=True, null=True)),
                ('key_info', models.TextField(blank=True, null=True)),
                ('specific_request', models.TextField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cprofile.company')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line', models.TextField()),
                ('locality', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('pin_code', models.CharField(max_length=6)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cprofile.company')),
            ],
        ),
        migrations.CreateModel(
            name='BankDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=50)),
                ('account_number', models.CharField(max_length=15)),
                ('ifsc_code', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cprofile.company')),
            ],
        ),
    ]