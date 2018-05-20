from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from .models import *
from django.db.models import Q

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

def album(request, id):
    album = Album.objects.get(id=id)
    songs = Song.objects.filter(album=album)
    return render(request, 'album.html', {'album':album, 'songs':songs})

def addSong(request, id):
    if request.method == "POST":
        title = request.POST.get('title')
        album = Album.objects.get(id=id)

        audio = request.FILES['audio']
        fs = FileSystemStorage()
        filename_audio = fs.save(audio.name, audio)
        uploaded_audio_url = fs.url(filename_audio)

        song = Song.objects.create(title=title, audio=audio, album=album)
        song.save()

        return redirect('/album/'+id)
    else:
        return redirect('/album/'+id)

def search(request):
    if request.method == "GET":
        searchText = request.GET.get('search')
        print(searchText)
        albums = Album.objects.filter()
        songResults = Song.objects.filter(Q(title__icontains=searchText))
        albumResults = Album.objects.filter(Q(title__icontains=searchText) | Q(artist__icontains=searchText) | Q(genre__icontains=searchText))
        searchCount = songResults.count() + albumResults.count()
        return render(request, 'search.html', {'albums':albums, 'songResults':songResults, 'albumResults':albumResults, 'searchCount':searchCount})
    return render(request, 'index.html', {})
