from django import forms
from django.forms.fields import IntegerField
from .models import match

class AddmatchForm(forms.ModelForm):
    home_team = forms.SelectMultiple()
    home_team_result =IntegerField()
    away_team = forms.SelectMultiple()
    away_team_result = forms.IntegerField()
    


    class Meta:
        model = match
        fields = ('home_team','home_team_result','away_team','away_team_result')