from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.http import request




class TechNews(models.Model):

  heading=models.CharField(max_length=70)
  paragraph1=models.TextField(max_length=1024)
  paragraph2=models.TextField(max_length=1024)
  timeline=models.DateField()
  author = models.CharField(max_length=20)
  validate=models.BooleanField(default=False)
 