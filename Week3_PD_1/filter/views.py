from django.shortcuts import render
import datetime

d = {
    "name": "Jabir",
    "age": 20,
    "city": "Dhaka",
    "course": [
        {"name": "Python", "price": 1000},
        {"name": "Java", "price": 2000},
        {"name": "C++", "price": 3000},
        {"name": "JavaScript", "price": 4000},
        {"name": "Ruby", "price": 5000},
        {"name": "PHP", "price": 6000},
        {"name": "C#", "price": 7000},
        {"name": "Swift", "price": 8000},
        {"name": "Kotlin", "price": 9000},
        {"name": "Go", "price": 10000},
    ],
    "lst": [
        "Python",
        "Java",
        "C++",
        "JavaScript",
        "Ruby",
        "PHP",
        "C#",
        "Swift",
        "Kotlin",
        "Go",
    ],
    "date": datetime.datetime.now(),
    "empty": "",
    "cut": "python-is-fun",
    'sentence': 'Python is Fun and Easy to Learn and it is a High Level Programming Language',
    "hml": "<h1>Python is Fun</h1>",
    "num": 1234567890,
    "phone": "+8801712345678",
    "url": "https://www.python.org/",}


def home(request):
    return render(request, "filter_home.html", d)


def about(request):
    return render(request, "about.html", d)


def contact(request):
    return render(request, "contact.html", d)


def template_filter(request):
    return render(request, "template_filter.html", d)
