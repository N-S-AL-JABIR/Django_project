from django.shortcuts import render,redirect, get_object_or_404
from .forms import AlbumForm
from Musician.forms import MusicianForm
from .models import Album 
from .models import Musician

def album_list(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AlbumForm()
    return render(request, 'album.html', {'form': form})    


def edit_musician(request, id):
    post = Musician.objects.get(pk=id)
    form = MusicianForm(instance=post)
    if request.method == "POST":
        form = MusicianForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, "musician.html", {"form": form,"id":id})


def edit_album(request, id):
    post = Album.objects.get(pk=id)
    form = AlbumForm(instance=post)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, "album.html", {"form": form, "id":id})


def delete_Musician(request, id):
    post = Musician.objects.get(pk=id)
    post.delete()
    return redirect("home")

    # musician = get_object_or_404(Musician, pk=id)
    # musician.delete()
    # return redirect("home")
