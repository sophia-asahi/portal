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
        # return redirect('home')
        return render(request, 'student/register.html')


def login(request):
    # if request.method == "POST":
    #     username = request.POST('username')
    #     pwd = request.POST('pwd')
    #
    #

    #postParams = {}
    if request.method == "POST":
        postParams = request.POST

        con = mysql.connector.connect(host="localhost", user="root", password="Asahi@123", database="studentportal",auth_plugin='mysql_native_password')
        cursor = con.cursor(buffered=True)
        username = postParams['username']
        pwd = postParams['pwd']
        sqlcommand = "select * from student_signup where username='" + username + "' and pwd='" + pwd + "'"
         #sqlcommand1 = "select pwd from student_signup"
        cursor.execute(sqlcommand)
         #cursor.execute(sqlcommand1)
        record = cursor.fetchone()
        print(record)
        first_name = postParams.get('first_name')
        last_name = postParams.get('last_name')
        department = postParams.get('department')
        cgpa = postParams.get('cgpa')
        age = postParams.get('age')
        address = postParams.get('address')
         #con1 =  mysql.connector.connect(host = "localhost",user="root",password = "Asahi@123",database="studentportal",auth_plugin='mysql_native_password')
         #cursor = con1.cursor(buffered=True)
         #check if record is null/None and if yes, then show that the credentials are wrong
         #if it returns a valid record (that is basically the student id), then return to home page with the complete user details (send the record object to home page)
        if record == None:
             return redirect("login")
        else:
            return render(request, 'student/details.html', {"username": username})

    return render(request, 'student/login.html')

def current(request):
    students = Signup.object.filter(record)
    return render (request,'student/details.html',{"students":students})

def logout(request):
    return redirect('home')