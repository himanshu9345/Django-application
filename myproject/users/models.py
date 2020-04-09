from django.db import models

# Create your models here.
from django.db import models
from django.contrib.postgres.fields import ArrayField
import os,time
from uuid import uuid4
import uuid
from django.utils.deconstruct import deconstructible
from django.contrib.auth.models import User
import json
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
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    desc = models.TextField()
    start_month_year = models.DateField()
    end_month_year =models.DateField()

    def startMonth(self):
        return self.start_month_year.strftime("%b")
    
    def endMonth(self):
        return self.end_month_year.strftime("%b")


    def split_lines(self):
        return self.desc.split("#")
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Experience._meta.fields if field.name!='user']
    
    
    
class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_name=models.CharField(max_length=40)
    percentage_you_know=models.IntegerField()
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Skill._meta.fields if field.name!='user']

class Award(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    award_name=models.CharField(max_length=100)
    award_place=models.CharField(max_length=100)
    describe_award = models.TextField()
    award_month_year = models.DateField()
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Award._meta.fields if field.name!='user']

class Publication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_title= models.CharField(max_length=200)
    publication_name= models.CharField(max_length=200)
    publication_date= models.DateField()
    publication_url = models.URLField()
    publication_description = models.TextField()
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Publication._meta.fields if field.name!='user']

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=200)
    project_description = models.TextField()
    project_url = models.URLField(default="")
    image_path = time.strftime('pics/%Y/%m/%d')
    project_image = models.ImageField(upload_to=PathAndRename(image_path))
    project_start_month_year = models.DateField()
    project_end_month_year =models.DateField()
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Project._meta.fields if field.name!='user']
    def startMonth(self):
        return self.project_start_month_year.strftime("%b")
    
    def endMonth(self):
        return self.project_end_month_year.strftime("%b")

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    college_name = models.CharField(max_length=200)
    degree_name = models.CharField(max_length=200)
    major_name = models.CharField(max_length=200)
    college_start_month_year = models.DateField()
    college_end_month_year =models.DateField()
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Education._meta.fields if field.name!='user']
    def startMonth(self):
        return self.college_start_month_year.strftime("%b")
    
    def endMonth(self):
        return self.college_end_month_year.strftime("%b")

def convertToCamelCase(word):
    return ' '.join(x.capitalize() or ' ' for x in word.split(' '))
class UserExtraDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image_path = time.strftime('profile/%Y/%m/%d')
    user_image = models.ImageField(upload_to=PathAndRename(image_path),default="default.png")
    user_interest = models.CharField(max_length=400,default="")
    user_address = models.CharField(max_length=200,default="")
    image_path = time.strftime('files/%Y/%m/%d')
    user_resume = models.FileField(upload_to=PathAndRename(image_path),default="resume.pdf")
    user_project_completed = models.IntegerField(default=0)
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in UserExtraDetails._meta.fields if field.name!='user']
    
    def get_interest(self):
        return json.dumps([convertToCamelCase(word)+"." for word in self.user_interest.split(",")])

class ContactDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_type=models.CharField(max_length=20)
    contact_profile_url=models.URLField(default="")
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in ContactDetails._meta.fields if field.name!='user']
 
