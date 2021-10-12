from django.urls import path
from . import views

app_name= 'matches'
urlpatterns=[
    path('',views.Addmatch, name='addmatch'),
   

]