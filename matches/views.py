from django.shortcuts import render
from .models import match
from .addmatch import AddmatchForm

# Create your views here.
def Addmatch(request):
    if request.method == 'POST':
        add = AddmatchForm(request.POST)
        if add.is_valid():
            team_name = add.cleaned_data['team_name']
            team_scores = add.cleaned_data['team_scores']
            team_goals = add.cleaned_data['team_goals']
            
            add.save()

    add = AddmatchForm()
    return render(request, 'teams/addteam.html',
    {'add':add})