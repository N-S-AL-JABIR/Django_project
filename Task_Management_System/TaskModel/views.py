from django.shortcuts import render, redirect
from . import forms
from .models import Task


def task(request):
    if request.method == "POST":
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_task")
    else:
        form = forms.TaskForm()
    return render(request, "add_task.html", {"form": form})


def edit_task(request, id):
    post = Task.objects.get(pk=id)
    form = forms.TaskForm(instance=post)
    if request.method == "POST":
        form = forms.TaskForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "add_task.html", {"form": form, "edit": True})


def delete_task(request, id):
    post = Task.objects.get(pk=id)
    post.delete()
    return redirect("home")


def view_task(request):
    post = Task.objects.all()
    # print(post)
    return render(request, "view_task.html", {"post": post})
