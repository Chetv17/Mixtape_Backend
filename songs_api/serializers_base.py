from rest_framework import serializers
from .models import Song


class SongSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title', 'artist', 'cover', 'album')