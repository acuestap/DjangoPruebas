from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.

class Formulario_francis(models.Model):
    name = models.CharField(max_length=100,blank=False)
    email = models.EmailField(max_length=200,blank=False)
    phone = models.IntegerField(max_length=30,blank=False)
    city = models.CharField(max_length=50,blank=True,null=True)
    state = models.CharField(max_length=50,blank=True,null=True)
    created_date = models.DateTimeField(default=timezone.now)
