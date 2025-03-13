from django.shortcuts import render
import mysql.connector as sql

def signup(request):
    if request.method == 'POST': 
        obj = sql.connect(host="localhost", user="root", password="system", database="auth")
        cursor = obj.cursor()

        n = request.POST.get('name', '')
        e = request.POST.get('email', '')
        p = request.POST.get('password', '')

        sqlquery = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
        cursor.execute(sqlquery, (n, e, p))
        obj.commit()

        cursor.close()
        obj.close()

        return render(request, 'signup.html', {'message': 'User registered successfully!'})

    return render(request, 'signup.html')
