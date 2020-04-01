from django.db import models
from users.models import User
# Create your models here.
class UserToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=20)
