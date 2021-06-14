from rest_framework import serializers

from youtube_search.models import YoutubeData


class YoutubeVideosSerializer(serializers.ModelSerializer):

    '''
        serializer to validate and retrive data
    '''

    class Meta:
        model = YoutubeData
        fields = '__all__'
