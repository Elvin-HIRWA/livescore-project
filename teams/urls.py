from django.urls import path
from . import views

app_name= 'teams'
urlpatterns=[
    path('',views.Addteam,name='addteam'),
    path('all',views.listofteams, name='listofteams'),
    path('<int:team_id>',views.teamdetail,name='teamdetail'),

]