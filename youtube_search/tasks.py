from celery import shared_task
from django.conf import settings

from celery import Celery

from youtube_search.utils import YoutubeAPIRequest

app = Celery()

@shared_task
def fetch_and_retrive_youtube_apis():
    '''
    Task to initiate youtube api

    '''
    YoutubeAPIRequest().initialise_and_process_request()

