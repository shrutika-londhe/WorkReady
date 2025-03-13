from django.shortcuts import render
import mysql.connector as sql

def homePage(request):
    return render(request, 'index.html')
