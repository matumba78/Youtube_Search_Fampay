from django.conf import settings
from googleapiclient import discovery
from googleapiclient.errors import HttpError
import apiclient
from datetime import datetime, timezone, timedelta
import os



from youtube_search.serializers import YoutubeVideosSerializer

from rest_framework.exceptions import ValidationError



class FetchYoutubeAPI:

    '''
        This class accepts api key and query and initialize them.
        Returns youtube data response object
    '''

    query = None
    part = "snippet"
    order = "date"
    max_result = 30
    published_date = None
    api_key = None

    def __init__(self, query=None, api_key=''):
        self.query = query
        self.published_date = None
        self.api_key = api_key

    def fetch_youtube_data(self):
        try:
            last_pub_date = self.get_timestamp()
            service = discovery.build("youtube", "v3", developerKey=self.api_key)
            youtube_request_object = service.search().list(q=self.query, part=self.part, order=self.order, maxResults=self.max_result,
                                                           publishedAfter=last_pub_date)
            return youtube_request_object
        except HttpError as err:
            return None

    def get_timestamp(self):
        past_time = datetime.utcnow() - timedelta(minutes=5)
        now_time = str(past_time.replace(tzinfo=timezone.utc)).split(' ')
        return f"{now_time[0]}T{now_time[1][:-6]}Z"


class YoutubeAPIRequest:

    def initialise_and_process_request(self):
        '''
        fetch and retrive youtube data and save them to db
        multiple keys are handled in case quota exhausted
        '''
        api_keys = settings.YOUTUBE_API_KEY
        query = settings.YOUTUBE_SEARCH_QUERY
        api_status = False
        for key in api_keys:
            try:
                response = FetchYoutubeAPI(query, key).fetch_youtube_data()
                res = response.execute()
                api_status = True
                for data in res["items"]:
                    result = {
                        "title": data.get("snippet", {}).get("title", ""),
                        "description": data.get("snippet", {}).get("snippet", ""),
                        "published_at": data.get("snippet", {}).get("publishedAt", ""),
                        "thumbnail_url": data.get("snippet", {}).get("thumbnails", {}).get("default", "").get("url", ""),
                        "video_id": data.get("id", {}).get("videoId", ""),
                        "channel_title": data.get("snippet", {}).get("channelTitle", ""),
                        "channel_id": data.get("snippet", {}).get("channelId", "")
                    }
                    try:
                        '''
                        validating data before saving so to avoid duplicacy
                        '''
                        youtube_data = YoutubeVideosSerializer(data=result)
                        if youtube_data.is_valid(raise_exception=True):
                            youtube_data.save()
                    except ValidationError:
                        continue
            except apiclient.errors.HttpError as err:
                print(err)

            if api_status:
                break









