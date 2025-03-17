from django.shortcuts import render
import mysql.connector as sql

def homePage(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')