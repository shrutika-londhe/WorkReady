from django.shortcuts import render
import mysql.connector as sql

def login(request):
    if request.method == 'POST': 
        obj = sql.connect(host="localhost", user="root", password="system", database="workready")
        cursor = obj.cursor()

        e = request.POST.get('email', '')
        p = request.POST.get('password', '')

     
        sqlquery = "SELECT * FROM users WHERE email = %s AND password = %s"
        cursor.execute(sqlquery, (e, p))
        result = cursor.fetchall()
       
        cursor.close()
        obj.close()

        if not result: 
            return render(request, 'error.html', {'message': 'Invalid credentials!'})
        else:  
            return render(request, 'index.html', {'message': 'Login successful!'})

    return render(request, 'login.html')
