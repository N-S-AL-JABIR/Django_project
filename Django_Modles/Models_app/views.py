from django.shortcuts import render, redirect
from . import models
def home(request):
    return render(request, 'home.html') 

def students(request):
    students = models.Students.objects.all()    
    return render(request, 'Create_Account.html', {'data': students})

def delete_student(request, roll_no):
    student = models.Students.objects.get(pk=roll_no)
    student.delete()
    return redirect('students')