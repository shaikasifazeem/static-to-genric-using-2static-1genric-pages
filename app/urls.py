from django.urls import path
from app.views import *
app_name='app'
urlpatterns=[
    path('rain/',rain,name='rain'),
    path('water/',water,name='water'),
]
