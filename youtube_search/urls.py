from django.urls import path
from . import views

urlpatterns = [
    path("get_videos/", views.YoutubeVideosListView.as_view(), name='get_videos')

]