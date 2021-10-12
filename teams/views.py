from django.shortcuts import render,get_object_or_404
from .models import team
from .addteam import AddTeamsForm
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def listofteams(request):
    teamlist = team.objects.all()
    template = loader.get_template('teams/allteams.html')
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
    return render(request, 'teams/addteam.html',
    {'add':add})

def teamdetail(request, team_id):

    #x = team.objects.get(pk=team_id)
    teamdetails = get_object_or_404(team, pk=team_id)
    return render(request, 'teams/teamdetails.html', 
    {'teamdetails':teamdetails})