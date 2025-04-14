from django.shortcuts import render


def home(request):
    d = {"name": "Jabir", "age": 20, "city": "Dhaka"}
    return render(request, "home.html", d)
