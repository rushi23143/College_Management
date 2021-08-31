from django.db import models

# Create your models here.
class StudentUser(models.Model):
    #id
    username = models.CharField('StudentUser name',max_length=50)
    email = models.CharField('StudentUser email', max_length=50)
    password = models.CharField('StudentUser Password', max_length=20)

class TeacherUser(models.Model):
    #id
    username = models.CharField('TeacherUser name',max_length=50)
    email = models.CharField('TeacherUser email', max_length=50)
    password = models.CharField('TeacherUser Password', max_length=20)

class Tenstudent(models.Model):
    name = models.ForeignKey(StudentUser, on_delete=models.CASCADE)
    marathi = models.IntegerField(max_length=20)
    hindi = models.IntegerField(max_length=20)
    english = models.IntegerField(max_length=20)
    maths = models.IntegerField(max_length=20)
    science = models.IntegerField(max_length=20)
    history = models.IntegerField(max_length=20)
    total = models.IntegerField(max_length=20)
    tenth = models.IntegerField(max_length=20)
    sport = models.CharField(max_length=20)
    
class Twelvestudent(models.Model):
    name = models.ForeignKey(StudentUser, on_delete=models.CASCADE)
    english = models.IntegerField(max_length=20)
    hindi = models.IntegerField(max_length=20)
    physics = models.IntegerField(max_length=20)
    chemistry = models.IntegerField(max_length=20)
    maths = models.IntegerField(max_length=20)
    computer = models.IntegerField(max_length=20)
    total = models.IntegerField(max_length=20)
    tenth = models.IntegerField(max_length=20)
    twelth = models.IntegerField(max_length=20)
    sport = models.CharField(max_length=20)
    
class Degreestudent(models.Model):
    name = models.ForeignKey(StudentUser, on_delete=models.CASCADE)
    tenth = models.IntegerField(max_length=20)
    twelth = models.IntegerField(max_length=20)
    first_year = models.IntegerField(max_length=20)
    second_year = models.IntegerField(max_length=20)
    third_year = models.IntegerField(max_length=20)
    degree_percentage = models.IntegerField(max_length=20)


