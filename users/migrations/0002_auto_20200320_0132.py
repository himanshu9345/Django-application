# Generated by Django 3.0.4 on 2020-03-20 01:32

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextradetails',
            name='user_address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='userextradetails',
            name='user_intrest',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='userextradetails',
            name='user_resume',
            field=models.FileField(default='resume.pdf', upload_to=users.models.PathAndRename('files/2020/03/20')),
        ),
    ]