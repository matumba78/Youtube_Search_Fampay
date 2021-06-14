import django_filters

from youtube_search.models import YoutubeData


class YoutubeVideosFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")
    description =django_filters.CharFilter(field_name="description", lookup_expr="icontains")

    class Meta:
        model = YoutubeData
        fields = ["title", "description"]