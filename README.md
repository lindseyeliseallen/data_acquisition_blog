# data_acquisition_blog

# YouTube Trending Topics Analysis

## Overview
This project uses the YouTube Data API to gather data on trending videos and analyze which topics generate the most engagement.

## Research Question
Which YouTube topics/categories receive the most engagement in trending videos?

## Data
- **Source:** YouTube Data API v3
- **Region:** United States
- **Observations:** 200 videos
- **Features:** title, channel, publish_date, category_id,view_count, like_count, comment_count

## Tools/Packages
- Python
- pandas
- googleapiclient.discovery
- dotenv
- matplotlib

## Ethics
The YouTube API provides public data in accordance with YouTube’s Terms of Service. No scraping of private information was performed. Data was scraped 50 observations at a time in order to stay in line with the request limit. 

## Files
- `trending_vids.py` — API script
- `data/youtube_trending_US.csv` — dataset
- `eda.ipynb` — analysis
