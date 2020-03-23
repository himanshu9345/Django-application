from django.db import models

# Create your models here.
from django.db import models
from django.contrib.postgres.fields import ArrayField
import os,time
from uuid import uuid4
import uuid
from django.utils.deconstruct import deconstructible
from django.contrib.auth.models import User

# Create your models here.

@deconstructible
class PathAndRename(object):
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        # eg: filename = 'my uploaded file.jpg'
        ext = filename.split('.')[-1]  #eg: 'jpg'
        uid = uuid.uuid4().hex[:10]    #eg: '567ae32f97'

        # eg: 'my-uploaded-file'
        new_name = '-'.join(filename.replace('.%s' % ext, '').split())

        # eg: 'my-uploaded-file_64c942aa64.jpg'
        renamed_filename = '%(new_name)s_%(uid)s.%(ext)s' % {'new_name': new_name, 'uid': uid, 'ext': ext}

        # eg: 'images/2017/01/29/my-uploaded-file_64c942aa64.jpg'
        return os.path.join(self.path, renamed_filename)

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.TextField()
    position = models.TextField()
    desc = models.TextField()
    start_year = models.CharField(max_length=4)
    end_year =models.CharField(max_length=4)

    def split_lines(self):
        return self.desc.split("#")
    
class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_name=models.CharField(max_length=40)
    percentage_you_know=models.IntegerField()

class Award(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    award_name=models.CharField(max_length=100)
    award_place=models.CharField(max_length=100)
    describe_award = models.TextField()
    award_year = models.CharField(max_length=4)

class Publication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_title= models.CharField(max_length=200)
    publication_name= models.CharField(max_length=200)
    publication_date= models.DateField()
    publication_url = models.URLField()
    publication_description = models.TextField()

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=200)
    project_description = models.TextField()
    project_url = models.URLField()
    image_path = time.strftime('pics/%Y/%m/%d')
    project_photo = models.ImageField(upload_to=PathAndRename(image_path))
    project_start_year = models.CharField(max_length=4)
    project_end_year =models.CharField(max_length=4)

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    college_name = models.CharField(max_length=200)
    degree_name = models.CharField(max_length=200)
    major_name = models.CharField(max_length=200)
    college_start_year = models.CharField(max_length=4)
    college_end_year =models.CharField(max_length=4)

class UserExtraDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image_path = time.strftime('profile/%Y/%m/%d')
    user_image = models.ImageField(upload_to=PathAndRename(image_path),default="default.png")
    user_interest = models.CharField(max_length=400,default="")
    user_address = models.CharField(max_length=200,default="")
    image_path = time.strftime('files/%Y/%m/%d')
    user_resume = models.FileField(upload_to=PathAndRename(image_path),default="resume.pdf")
    user_project_completed = models.IntegerField(default=0)