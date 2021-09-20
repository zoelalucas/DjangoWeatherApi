from django.urls import path

from .views import home

app_name='weather'

urlpatterns = [
    path('',home, name='home')
]
