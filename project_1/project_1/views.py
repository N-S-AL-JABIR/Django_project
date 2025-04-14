from django.http import HttpResponse


def contact(req):
    return HttpResponse("hello Jabir")


def home(request):
    return HttpResponse("MY Home")
