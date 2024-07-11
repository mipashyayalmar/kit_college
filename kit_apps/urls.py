from django.contrib import admin
from django.urls import path
from kit_apps import views
from kit_apps.views import home, suggestion_list,event

urlpatterns = [
    path('home/', home, name='home'),
    path('suggestions/', suggestion_list, name='suggestion_list'),
    
]