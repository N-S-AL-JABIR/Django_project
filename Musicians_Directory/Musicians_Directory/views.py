from django.shortcuts import render
from Album.models import Album
def home(request):
    post = Album.objects.all()
    return render(request, 'home.html', {'data': post})
