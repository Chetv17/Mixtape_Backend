from django.db import models
from playlists_api.models import Playlist

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=255, blank=True)
    artist = models.CharField(max_length=255, blank=True)
    cover = models.CharField(max_length=255, blank=True)
    album = models.CharField(max_length=255, blank=True)
    playlist = models.ForeignKey(Playlist, related_name='songs', null=True, on_delete=models.SET_NULL)
