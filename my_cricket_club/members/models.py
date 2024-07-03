from django.db import models
#create your models here:
from django.db import  models
class Member(models.model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)

