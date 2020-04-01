# Generated by Django 3.0.4 on 2020-03-23 00:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0006_auto_20200321_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_photo',
            field=models.ImageField(upload_to=users.models.PathAndRename('pics/2020/03/23')),
        ),
        migrations.AlterField(
            model_name='userextradetails',
            name='user_image',
            field=models.ImageField(default='default.png', upload_to=users.models.PathAndRename('profile/2020/03/23')),
        ),
        migrations.AlterField(
            model_name='userextradetails',
            name='user_resume',
            field=models.FileField(default='resume.pdf', upload_to=users.models.PathAndRename('files/2020/03/23')),
        ),
    ]
