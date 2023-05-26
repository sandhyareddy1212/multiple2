from django.urls import path
from csk.views import *
app_name='swathi'
urlpatterns=[
    path('msd/',msd,name='msd'),
]