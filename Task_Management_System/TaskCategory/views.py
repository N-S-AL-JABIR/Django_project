from django.shortcuts import render, redirect
from . import forms


def task_category(request):
    if request.method == "POST":
        form = forms.TaskCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_task_category")
    else:
        form = forms.TaskCategoryForm()
    return render(request, "add_task_category.html", {"form": form})
