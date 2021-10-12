from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class match(models.Model):
     home_team= models.CharField(max_length=200)
     home_team_result= models.IntegerField()
     away_team= models.CharField(max_length=200)
     away_team_result= models.IntegerField()
     kickof=models.DateTimeField('started from')
    
    