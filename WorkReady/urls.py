"""
URL configuration for WorkReady project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from WorkReady.views import homePage
from login.views import login
from signup.views import signup
from WorkReady.views import intern
from WorkReady.views import job


urlpatterns = [
    path('', homePage),
    path('login',login),
    path('signup',signup),
    path('intern', intern),
    path('job', job), 
]
