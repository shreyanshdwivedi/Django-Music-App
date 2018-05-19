from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from .models import *

# Create your views here.

def index(request):
    albums = Album.objects.filter()
    return render(request, 'index.html', {'albums':albums})

def addAlbum(request):
    if request.method == "POST":
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        genre = request.POST.get('genre')

        logo = request.FILES['logo']
        fs = FileSystemStorage()
        filename_logo = fs.save(logo.name, logo)
        uploaded_logo_url = fs.url(filename_logo)

        album = Album.objects.create(title=title, artist=artist, genre=genre, logo=logo)
        album.save()

        return redirect('app:index')
    else:
        return render(request, 'addAlbum.html', {})

