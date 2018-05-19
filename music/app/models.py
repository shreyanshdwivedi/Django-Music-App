from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Album(models.Model):
    title  = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    logo = models.FileField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=250)
    audio = models.FileField(blank=True, null=True)
    album = models.OneToOneField(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class FavoriteSong(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    song = models.OneToOneField(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " " + self.song.title

class FavoriteAlbum(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    album = models.OneToOneField(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " " + self.album.title