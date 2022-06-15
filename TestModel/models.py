from unicodedata import name
from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=20)
# Create your models here.
