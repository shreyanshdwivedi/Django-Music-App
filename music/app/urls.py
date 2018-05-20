from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addAlbum$', views.addAlbum, name='addAlbum'),
    url(r'^search$', views.search, name='search'),
    url(r'^album/(?P<id>\w+)$', views.album, name='album'),
    url(r'^addSong/(?P<id>\w+)$', views.addSong, name='addSong'),
]
