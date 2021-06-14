from django.db import models

# Create your models here.


class YoutubeData(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    published_at = models.DateTimeField()
    thumbnail_url = models.CharField(max_length=200, null=True, blank=True)
    video_id = models.CharField(max_length=100, unique=True)
    channel_id = models.CharField(max_length=200)
    channel_title = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

