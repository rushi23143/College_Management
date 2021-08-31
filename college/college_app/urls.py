from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.navigate, name='navigate'),
    path('student/student_login/', views.student_login, name='student_login'),
    path('student/student_signup/', views.student_signup, name='student_signup'),
    path('student/student_page/', views.student_page, name='student_page'),
    path('student/tenstudent/', views.tenstudent, name='tenstudent'),
    path('student/twelvestudent/', views.twelvestudent, name='twelvestudent'),
    path('student/degreestudent/', views.degreestudent, name='degreestudent'),
    #path('export_users_csv/', views.export_users_csv),
    path('student/student_logout/', views.student_logout, name='student_logout'),
    path('teacher/teacher_login/', views.teacher_login, name='teacher_login'),
    path('teacher/teacher_signup/', views.teacher_signup, name='teacher_signup'),
    path('teacher/teacher_page/', views.teacher_page, name='teacher_page'),
    path('teacher/teacher_logout/', views.teacher_logout, name='teacher_logout'),
]