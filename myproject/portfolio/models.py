from django.db import models
from django.contrib.postgres.fields import ArrayField
import os
from uuid import uuid4
# Create your models here.
def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(path, filename)
    return wrapper

class Experience(models.Model):
    company = models.TextField()
    position = models.TextField()
    desc = models.TextField()
    start_year = models.CharField(max_length=4)
    end_year =models.CharField(max_length=4)

    def split_lines(self):
        return self.desc.split("#")
    
class Skill(models.Model):
    skill_name=models.CharField(max_length=40)
    percentage_you_know=models.IntegerField()

class Award(models.Model):
    award_name=models.CharField(max_length=100)
    award_place=models.CharField(max_length=100)
    describe_award = models.TextField()
    award_year = models.CharField(max_length=4)

class Publication(models.Model):
    publication_title= models.CharField(max_length=200)
    publication_name= models.CharField(max_length=200)
    publication_date= models.DateField()
    publication_url = models.URLField()
    publication_description = models.TextField()

class Project(models.Model):
    project_title = models.CharField(max_length=200)
    project_description = models.TextField()
    project_url = models.URLField()
    project_photo = models.ImageField(upload_to=path_and_rename('pics'))
    project_start_year = models.CharField(max_length=4)
    project_end_year =models.CharField(max_length=4)
