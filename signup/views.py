from django.shortcuts import render
import mysql.connector as sql

def signup(request):
    if request.method == 'POST': 
        obj = sql.connect(host="localhost", user="root", password="system", database="workready")
        cursor = obj.cursor()

        fn = request.POST.get('firstname', '')
        ln= request.POST.get('lastname', '')
        e = request.POST.get('email', '')
        p = request.POST.get('password', '')

        sqlquery = "INSERT INTO users (firstname,lastname, email, password) VALUES (%s, %s, %s, %s)"
        cursor.execute(sqlquery, (fn,ln, e, p))
        obj.commit()

        cursor.close()
        obj.close()

        return render(request, 'signup.html', {'message': 'User registered successfully!'})

    return render(request, 'signup.html')
