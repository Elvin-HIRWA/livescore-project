from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


TEAM_CHOICES = (

          ('liverpool','LIVERPOOL'),
          ('chelsea', 'CHELSEA'),
          ('manu','MANU'),
          ('mancity','MANCITY'),
          ('arsenal','ARSENAL'),
          ('spurs','SPURS'),
          ('leicester', 'LEICESTER'),
          ('wolves','WOLVES'),
          ('southmpton','SOUTHAMPTON'),
          ('watford','WATFORD'),
          ('leeds','LEEDS'),
          ('bha', 'BHA'),
          ('everton','EVERTON'),
          ('astonvilla','ASTONVILLA'),
          ('brentford','BRENTFORD'),
          ('westham','WESTHAM'),
          ('crystalpalace', 'CRYSTALPALACE'),
          ('burnley','BURNLEY'),
          ('newcastle','NEWCASTLE'),
          ('norwich','NORWICH'),
     )

class match(models.Model):

          home_team = models.CharField(max_length=200, choices=TEAM_CHOICES, default='liverpool')
          home_team_result= models.IntegerField()
          away_team = models.CharField(max_length=200, choices=TEAM_CHOICES, default='liverpool')
          away_team_result= models.IntegerField()
         
          def __str__(self):
               return self.home_team 
    
    