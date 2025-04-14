from django.shortcuts import render, redirect
from . import forms
from .models import Post


def add_posts(request):
    if request.method == "POST":
        form = forms.Post(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_posts")
    else:
        form = forms.Post()
    return render(request, "add_post.html", {"form": form})

def edit_post(request,id):
    post = Post.objects.get(pk=id)
    form = forms.Post(instance=post)
    if request.method == "POST":
        form = forms.Post(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "add_post.html", {"form": form})

def delete_post(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect("home")
