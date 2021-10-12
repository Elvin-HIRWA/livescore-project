from django.db import models

# Create your models here.
class team(models.Model):
    team_name=models.CharField(max_length=200)
    team_scores=models.IntegerField()
    team_goals= models.IntegerField()
    def __str__(self):
        return self.team_name
   

class teamdetail(models.Model):
    team_id=models.ForeignKey(team, on_delete=models.CASCADE)
    team_manager=models.CharField(max_length=500)
    
    def __str__(self):
        return str(self.team_manager)