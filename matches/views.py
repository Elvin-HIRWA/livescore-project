from django.shortcuts import render
from .models import match
from .addmatch import AddmatchForm

# Create your views here.
def Addmatch(request):
    if request.method == 'POST':
        add = AddmatchForm(request.POST)
        if add.is_valid():
            home_team = add.cleaned_data['home_team']
            home_team_result = add.cleaned_data['home_team_result']
            away_team = add.cleaned_data['away_team']
            away_team_result = add.cleaned_data['away_team_result']
           
            add.save()

    add = AddmatchForm()
    return render(request, 'matches/addmatch.html',
    {'add':add})