from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.list import ListView
from django.contrib.sessions.models import Session
from django.contrib import auth
from .models import *
import csv
#from college_app.functions import handle_uploaded_file  #functions.py
#from college_app.forms import StudentData #forms.py

# Create your views here.
def navigate(request):
    if request.method == "POST":
        button = request.POST['button']
        if button == 'teacher':
            return redirect('teacher_login')
        elif button == 'student':
            return redirect('student_login')
    return render(request, 'navigate.html')

def student_login(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        count = StudentUser.objects.filter(email=email,password=password).count()
        if count >0:
            request.session['is_logged'] = True
            request.session['user_id'] = StudentUser.objects.values('id').filter(email=email,password=password)[0]['id']
            return redirect('student_page')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('student_login')
    return render(request, 'student/student_login.html')

def student_signup(request):
    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        obj = StudentUser(username=username,email=email,password=password)
        obj.save()
        messages.success(request, 'You are registered successfully')
        return redirect('student_login')
    return render(request, 'student/student_signup.html')

def student_logout(request):
    auth.logout(request)
    return redirect('student_login')

def teacher_login(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        count = TeacherUser.objects.filter(email=email,password=password).count()
        if count >0:
            request.session['is_logged'] = True
            request.session['user_id'] = TeacherUser.objects.values('id').filter(email=email,password=password)[0]['id']
            return redirect('teacher_page')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('teacher_login')
    return render(request, 'teacher/teacher_login.html')

def teacher_signup(request):
    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        obj = TeacherUser(username=username,email=email,password=password)
        obj.save()
        messages.success(request, 'You are registered successfully')
        return redirect('teacher_login')
    return render(request, 'teacher/teacher_signup.html')

def teacher_logout(request):
    auth.logout(request)
    return redirect('teacher_login')

def student_page(request):
    if request.session.has_key('is_logged'):
        return render(request, 'student/student_page.html')
    return redirect('student_login')
"""
def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="user.csv"'

    writer = csv.writer(response)
    writer.writerow(['name', 'ten', 'twelve', 'degree'])

    userss = StudentData.objects.all().values_list('name', 'ten', 'twelve', 'degree')
    for user in userss:
        writer.writerow(user)

    return response
"""
def teacher_page(request):
    if request.session.has_key('is_logged'):
        return render(request, 'teacher/teacher_page.html')
    return redirect('teacher_login')

def tenstudent(request):
    if request.method == "POST":
        name = request.POST['name']
        marathi = request.POST['marathi']
        hindi = request.POST['hindi']
        english = request.POST['english']
        maths = request.POST['maths']
        science = request.POST['science']
        history = request.POST['history']
        total = request.POST['total']
        tenth = request.POST['tenth']
        sport = request.POST['sport']
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="tenstudent.csv"'

        writer = csv.writer(response)
        writer.writerow(['name', 'marathi', 'hindi', 'english', 'maths', 'science', 'history', 'total','tenth', 'sport'])
        
        tenstudent = [[name, marathi, hindi, english, maths, science, history, total,tenth, sport]]
        
        for user in tenstudent:
            writer.writerow(user)

        return response
    return render(request, 'student/tenstudent.html')

def twelvestudent(request):
    if request.method == "POST":
        name = request.POST['name']
        english = request.POST['english']
        hindi = request.POST['hindi']
        physics = request.POST['physics']
        chemistry = request.POST['chemistry']
        maths = request.POST['maths']
        computer = request.POST['computer']
        total = request.POST['total']
        tenth = request.POST['tenth']
        twelth = request.POST['twelth']
        sport = request.POST['sport']

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="twelvesudent.csv"'

        writer = csv.writer(response)
        writer.writerow(['name', 'english', 'hindi', 'physics', 'chemistry', 'maths', 'computer','total','tenth', 'twelth', 'sport'])
        
        twelvesudent = [[name, english, hindi, physics, chemistry, maths, computer, total, tenth, twelth, sport]]
        for user in twelvesudent:
            writer.writerow(user)

        return response
    return render(request, 'student/twelvestudent.html')

def degreestudent(request):
    if request.method == "POST":
        name = request.POST['name']
        tenth = request.POST['tenth']
        twelth = request.POST['twelth']
        first_year = request.POST['first']
        second_year = request.POST['second']
        third_year = request.POST['third']
        degree_percentage = request.POST['degree']
        

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="degreestudent.csv"'

        writer = csv.writer(response)
        writer.writerow(['name', 'tenth', 'twelth', 'first_year', 'second_year', 'third_year', 'degree_percentage'])

        degreestudent = [[name, tenth, twelth, first_year, second_year, third_year, degree_percentage]]

        for user in degreestudent:
            writer.writerow(user)

        return response
    return render(request, 'student/degreestudent.html')
