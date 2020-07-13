from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator,MaxLengthValidator

# Create your models here.
class User_info(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 20)
    age = models.IntegerField(validators = [MinLengthValidator(2),MaxLengthValidator(3)])
