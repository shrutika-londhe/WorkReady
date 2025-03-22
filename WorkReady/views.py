from django.shortcuts import render
import mysql.connector as sql

def homePage(request):
    return render(request, 'index.html')

def intern(request):
    return render(request,'internship.html')

def job(request):
    return render(request,'job.html')

def course(request):
    return render(request,'course.html')