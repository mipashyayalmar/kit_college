"""
URL configuration for kit_projects project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from kit_apps import views

# from kit_apps.views import get_sugetion

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("",views.home),
#     path('gets/',views.get_sugetion),
# ]




from django.contrib import admin
from django.urls import path
from kit_apps import views
from kit_apps.views import home, suggestion_list
from kit_apps.views import suggestion_table,event


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('suggestions/', suggestion_list, name='suggestion_list'),
     path('suggestion-table/', suggestion_table, name='suggestion_table'),
     path('events/',event,name='events'),
     ]