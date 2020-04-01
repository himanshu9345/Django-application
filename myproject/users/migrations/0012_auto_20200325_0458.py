# Generated by Django 3.0.4 on 2020-03-25 04:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0011_auto_20200324_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_image',
            field=models.ImageField(upload_to=users.models.PathAndRename('pics/2020/03/25')),
        ),
        migrations.AlterField(
            model_name='userextradetails',
            name='user_image',
            field=models.ImageField(default='default.png', upload_to=users.models.PathAndRename('profile/2020/03/25')),
        ),
        migrations.AlterField(
            model_name='userextradetails',
            name='user_resume',
            field=models.FileField(default='resume.pdf', upload_to=users.models.PathAndRename('files/2020/03/25')),
        ),
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_linkedin', models.URLField(default='')),
                ('user_twitter', models.URLField(default='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
