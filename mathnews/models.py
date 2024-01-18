from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.http import request




class TechNews(models.Model):

  heading=models.CharField(max_length=70)
  part_1=models.TextField(max_length=1024)
  part_2=models.TextField(max_length=1024)
  timeline=models.DateField()
  author = models.CharField(max_length=20)
  validate=models.BooleanField(default=False)
  star = models.ManyToManyField(User, related_name='star', default=None, blank=True)
  

  @property
  def number_of_stars(self):
        return self.star.count()
  
  @property
  def number_of_clouds(self):
        return self.cloud.count()


LIKE_CHOICES=(
 ('Star', 'Star'),
 ('Unstar', 'Unstar')    
)

class Like(models.Model):
     user= models.ForeignKey(User, on_delete=models.CASCADE)
     news= models.ForeignKey(TechNews, on_delete=models.CASCADE)
     value= models.CharField(choices=LIKE_CHOICES, default='star', max_length=10)
     
     def __str__(self) :
         return str(self.news)