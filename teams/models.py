from django.db import models

# Create your models here.
class team(models.Model):
    team_name=models.CharField(max_length=200)
    team_scores=models.IntegerField()
    team_goals= models.IntegerField()
    def __str__(self):
        return self.team_name
   