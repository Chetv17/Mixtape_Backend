from .serializers_base import PlaylistSerializerBase
from songs_api.serializers_base import SongSerializerBase

class PlaylistSerializer(PlaylistSerializerBase):
    songs = SongSerializerBase(many=True, required=False)
    class Meta(PlaylistSerializerBase.Meta):
        fields = PlaylistSerializerBase.Meta.fields + ('songs',)