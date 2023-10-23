from django.db import models
from django.db.models import When
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
import string
import random

def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Job.objects.filter(code = code).count() == 0:
            break

    return code

class Contact(models.Model):
    msgid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, default='')
    email = models.CharField(max_length=300, default='')
    phone = models.CharField(max_length=300, default='')
    desc = models.CharField(max_length=300, default='')


class User(AbstractUser):
    # user_name = models.CharField(max_length=20, default='', unique=True)
    # first_name = models.CharField(max_length=20, default='')
    # last_name = models.CharField(max_length=20, default='')
    # email = models.EmailField(max_length=100)
    age = models.IntegerField(default=1)
    skillset = models.CharField(default = "Hello",null=True,blank=True,max_length=400)
    # password = models.CharField(max_length=20, default='')
    # password_again = models.CharField(max_length=20, default='')
    # def __str__(self):
    #     return self.user_name

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
        
    
class Job(models.Model):
    code = models.CharField(max_length=8, default=generate_unique_code, unique=True)
    requirements = models.TextField()
    description = models.TextField()
    mail = models.EmailField(max_length=100)
    # job_title = models.TextField()


class Organisation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    helpline = models.IntegerField()
    mail = models.EmailField(max_length=100)
    
