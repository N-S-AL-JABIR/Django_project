from django.shortcuts import render
from . import forms

def home(request):
    return render(request, "home.html")


def form(request):
    return render(request, "form.html")


def about(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get("username")
        email = request.POST.get("useremail")
        Select = request.POST.get("select")
        return render(request, "about.html", {"name": name, "email": email ,"select": Select})
    else:
        return render(request, "about.html")

def django_form(request):
    if request.method == "POST":
        form = forms.ContactForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open("django-forms.html" + file.name, "wb+") as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
    else:
        form = forms.ContactForm()
    return render(request, "django-forms.html", {"form": form})   

def student_form(request):
    if request.method == "POST":
        form = forms.StudentForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = forms.StudentForm()
    return render(request, "student_forms.html", {"form": form})