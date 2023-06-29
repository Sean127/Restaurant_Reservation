"""reservation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from thebest.views import get_reservation, homepage, get_menu, get_open_times, get_confirm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('menu', get_menu, name='menu'),
    path('open_times', get_open_times, name='open_times'),
    path('confirm', get_confirm, name='confirm'),
    path('reservation', get_reservation, name='reservation'),
]
