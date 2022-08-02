# Generated by Django 4.0.5 on 2022-08-01 12:24

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_statutorycompliance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pendingactionable',
            old_name='clientRemarks',
            new_name='client_remarks',
        ),
        migrations.AddField(
            model_name='pendingactionable',
            name='created_on',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='watchoutpoint',
            name='created_on',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2022, 8, 1, 12, 24, 41, 155980, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
