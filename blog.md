# Data Acquisition Project: Finding YouTube Trends by Topic

## Introduction

For my data acquisition project, I wanted to explore what kinds of videos are trending on YouTube in the United States. YouTube is one of the most popular platforms for videos and I was curious whether certain categories dominate the trending page. I also wanted to see how video engagement (views, likes, comments) differs by category.  

This project gave me a chance to learn about working with APIs, cleaning data, and doing a simple exploratory data analysis. These are all skills that are useful for real-world data projects.  

## Motivating Question

My main question was: *Which categories of videos are trending on YouTube and how does engagement vary by category?*

To answer this, I decided to collect the most popular videos in the US using the YouTube Data API. I focused on the US to simplfy and narrow down the data, but the same method could work for other countries.  

---
## Ethics

I used the YouTube Data API v3 which is publicly available and allows developers to get video statistics without violating YouTube’s terms of service. I created an API key through my Google account, which was free. I kept it private by storing it in a `.env` file. I made sure not to scrape any web pages directly because YouTube’s terms of service does not allow scraping from their website. Using the official API is the safest and most reliable way to get this data. The API has a request limit of 50 so I made sure to only request 50 at a time. I only requested the total of what I needed for the project (200 videos) and added a small delay between requests to avoid hitting limits or overwhelming the server. All the video data is publically available. I did not collect any private or personal information about the creators of the videos. 

---
## Steps to Gather the Data

Here’s a simple overview of what I did:

1. **Set up my Python environment**  
   I created a new project folder with subfolder for the data and all the files I needed, then opened it in VSCode.  

2. **Installed packages**  
   I installed `pandas` for data analysis, `googleapiclient.discovery` for the YouTube API, and `dotenv` for loading my API key from `.env`.  

3. **Connected to the YouTube API**  
   Using my API key, I wrote a Python function that finds trending videos. I set the API to get 50 videos per request (the maximum allowed per API call) and looped until I collected around 200 videos.

4. **Got the trending videos using the YouTube API**
   I used a Python function to follow my limit of requests and get my observations. I chose the region `"US"` and asked for information like the video title, channel name, number of views, likes, comments, publish date, and category ID. Each video’s information was stored in a list of dictionaries. I then converted the list into a pandas DataFrame so it was easy to work with and save. I also added a small pause between requests so I didn’t hit the API too quickly.

5. **Saved the data as a CSV**  
   After collecting the data, I saved it in `data/youtube_trending_US.csv`. This CSV includes 200 rows of video data with 7 these columns:
   - `title` – the video title  
   - `channel` – the channel name  
   - `publish_date` – when the video was uploaded  
   - `category_id` – a number representing the video category (which I later matched to category names) 
   - `view_count`, `like_count`, `comment_count` – engagement measurements  

6. **Mapped category IDs to names**  
   The API returns category IDs as numbers so I created a dictionary to map them to human-readable names (`10` = `"Music"`, `20` = `"Gaming"`). I found the names that match the category IDs on the Youtube API. I added this as a new column `category_name` so that you could actually see it in the EDA.  

---
