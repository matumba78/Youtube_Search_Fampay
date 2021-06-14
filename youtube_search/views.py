import django_filters.rest_framework as filters

from rest_framework import generics

from youtube_search.filters import YoutubeVideosFilter
from youtube_search.models import YoutubeData
from youtube_search.pagination import YoutubeVideosPagination
from youtube_search.serializers import YoutubeVideosSerializer


class YoutubeVideosListView(generics.ListAPIView):
    serializer_class = YoutubeVideosSerializer
    queryset = YoutubeData.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class =YoutubeVideosFilter
    ordering = ('-published_at')
    pagination_class = YoutubeVideosPagination





