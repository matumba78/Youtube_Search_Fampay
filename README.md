# Description
        To make an API to fetch latest videos sorted in reverse chronological
        order of their publishing date-time from YouTube for a given tag/search
        query in a paginated response

## Approach
        Used RabbitMQ , Celery to perform async process for fetching data from youtube every 5 mins

## Running the project
        Clone the project
        Install python 3.7 
        Install Docker 2.2
        Get api keys from google developer account and fill it in video_search/settings/YOUTUBEAPI_KEYS 
        run the following commands:
            docker-compose build
            docer-compose up
        
        
