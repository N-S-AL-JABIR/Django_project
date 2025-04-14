from django.shortcuts import render, redirect
from . import forms


def add_categories(request):
    if request.method == "POST":
        form = forms.CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_categories")
    else:
        form = forms.CategoryForm()
    return render(request, "add_categories.html", {"form": form})
