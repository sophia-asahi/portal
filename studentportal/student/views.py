import mysql.connector
from django.shortcuts import render, redirect,HttpResponse
from .models import Signup
from django.contrib import messages
from django.db import connections


def home(request):
    return render(request, 'student/home.html')


def register(request):
    if request.method == 'POST':
        saverecord = Signup()
        saverecord.username = request.POST.get('username')
        saverecord.pwd = request.POST.get('pwd')
        saverecord.first_name = request.POST.get('first_name')
        saverecord.last_name = request.POST.get('last_name')
        saverecord.department = request.POST.get('department')
        saverecord.cgpa = request.POST.get('cgpa')
        saverecord.age = request.POST.get('age')
        saverecord.address = request.POST.get('address')
        saverecord.save()
        messages.success(request, 'Registered Successfully!!!')
        return render(request, 'student/register.html')

    else:
        # return re
       return render(request, 'student/register.html')


def login(request):
    # if request.method == "POST":
    #     username = request.POST('username')
    #     pwd = request.POST('pwd')
    #postParams = {}
    if request.method == "POST":
        postParams = request.POST

        con = mysql.connector.connect(host="localhost", user="root", password="Asahi@123", database="studentportal",auth_plugin='mysql_native_password')
        cursor = con.cursor(buffered=True)
        username = postParams['username']
        pwd = postParams['pwd']
        sqlcommand = "select * from student_signup where username='" + username + "' and pwd='" + pwd + "'"

        cursor.execute(sqlcommand)

        record = cursor.fetchone()

        if record == None:
            return render(request, 'student/login.html')

        else:
            print(record)
            saverecord = Signup()  # filter,() ,all -same output
            saverecord.first_name = record[3]
            saverecord.last_name = record[4]
            saverecord.department = record[5]
            saverecord.cgpa = record[6]
            saverecord.age = record[7]
            saverecord.address = record[8]
            return render(request, 'student/details.html', {"saverecord": saverecord})

    return render(request, 'student/login.html')


def details(request):
     return request('student/details.html')


def logout(request):
    return redirect('home')