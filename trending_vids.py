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
