from django.urls import path
from . import views

app_name= 'teams'
urlpatterns=[
    path('hirwa',views.Addteam,name='addteam'),
    path('',views.listofteams, name='listofteams'),
    #path('<int:cour>/yourchoice/',views.yourchoice,name='yourchoice')

]