from django.urls import path
from sports.views import *
app_name = 'nothing'

urlpatterns =[
    path('cricket/',cricket,name='cricket'),
    
]