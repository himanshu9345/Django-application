# Generated by Django 3.0.4 on 2020-03-20 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200320_0134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userextradetails',
            old_name='user_intrest',
            new_name='user_interest',
        ),
    ]
