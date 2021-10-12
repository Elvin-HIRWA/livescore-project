from django.shortcuts import render
from .models import team
from .addteam import AddTeamsForm
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def listofteams(request):
    teamlist = team.objects.all()
    template = loader.get_template('teams/addteam.html')
    context={
        'teamlist':teamlist
    }
    return HttpResponse(template.render(context, request))

def Addteam(request):
    if request.method == 'POST':
        add = AddTeamsForm(request.POST)
        if add.is_valid():
            team_name = add.cleaned_data['team_name']
            team_scores = add.cleaned_data['team_scores']
            team_goals = add.cleaned_data['team_goals']
            
            add.save()

    add = AddTeamsForm()
    return render(request, 'teams/addteam.html',{'add':add})