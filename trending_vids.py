from googleapiclient.discovery import build
from dotenv import load_dotenv
import pandas as pd
import time
import os


load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY") 
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)


def get_trending_videos(region="US", total_results=200):
    videos = []
    next_page_token = None

    while len(videos) < total_results:
        request = youtube.videos().list(
            part="snippet,statistics",
            chart="mostPopular",
            regionCode=region,
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()

        for video in response["items"]:
            videos.append({
                "title": video["snippet"]["title"],
                "channel": video["snippet"]["channelTitle"],
                "publish_date": video["snippet"]["publishedAt"],
                "category_id": video["snippet"]["categoryId"],
                "view_count": video["statistics"].get("viewCount"),
                "like_count": video["statistics"].get("likeCount"),
                "comment_count": video["statistics"].get("commentCount")
            })

        next_page = response.get("nextPageToken")
        if not next_page:
            break

        time.sleep(1)

    return pd.DataFrame(videos)