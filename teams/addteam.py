from django import forms
from .models import team

class AddTeamsForm(forms.ModelForm):
    team_name = forms.CharField()
    team_scores = forms.IntegerField()
    team_goals = forms.IntegerField()

    class Meta:
        model = team
        fields = ('team_name','team_scores','team_goals')