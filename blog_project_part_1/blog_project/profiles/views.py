from django.shortcuts import render, redirect
from . import forms


def add_profiles(request):
    if request.method == "POST":
        form = forms.ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_author")
    else:
        form = forms.ProfileForm()
    return render(request, "add_profiles.html", {"form": form})
