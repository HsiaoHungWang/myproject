# Generated by Django 5.0.6 on 2024-08-06 11:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_remove_member_member_address_member_member_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='member_avatar',
            field=models.CharField(default='empty.png', max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 6, 19, 15, 44, 6462)),
        ),
    ]