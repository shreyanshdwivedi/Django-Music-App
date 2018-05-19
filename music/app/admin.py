from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(FavoriteAlbum)
admin.site.register(FavoriteSong)