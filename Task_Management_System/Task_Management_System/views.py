from django.shortcuts import render
from TaskModel.models import Task


def home(request):
    post = Task.objects.all()
    print(post)
    return render(request, "home.html", {"post": post})
