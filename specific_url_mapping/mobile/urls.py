from django.urls import path
from mobile.views import *
app_name = 'something'

urlpatterns=[
    path('vivo/',vivo,name='vivo'),

]