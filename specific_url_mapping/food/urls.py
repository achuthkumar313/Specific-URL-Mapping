from django.urls import path
from food.views import *
app_name = 'Anything'

urlpatterns = [
    path('biriyani/',biriyani,name='biriyani'),

]