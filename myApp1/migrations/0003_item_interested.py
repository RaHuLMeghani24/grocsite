# Generated by Django 4.0.3 on 2022-03-22 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp1', '0002_remove_client_fullname_client_phone_no_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='interested',
            field=models.PositiveIntegerField(default=0),
        ),
    ]