# Data Acquisition Project: Finding YouTube Trends by Topic

## Introduction

For my data acquisition project, I wanted to explore what kinds of videos are trending on YouTube in the United States. YouTube is one of the most popular platforms for videos and I was curious whether certain categories dominate the trending page. I also wanted to see how video engagement (views, likes, comments) differs by category.  

This project gave me a chance to learn about working with APIs, cleaning data, and doing a simple exploratory data analysis. These are all skills that are useful for real-world data projects.  

## Motivating Question

My main question was: *Which categories of videos are trending on YouTube and how does engagement vary by category?*

To answer this, I decided to collect the most popular videos in the US using the YouTube Data API. I focused on the US to simplfy and narrow down the data, but the same method could work for other countries.  

---
## Ethics

I used the YouTube Data API v3 which is publicly available and allows developers to get video statistics without violating YouTube’s terms of service. I created an API key through my Google account, which was free. I kept it private by storing it in a `.env` file. I made sure not to scrape any web pages directly because YouTube’s terms of service does not allow scraping from their website. Using the official API is the safest and most reliable way to get this data. The API has a request limit of 50 so I made sure to only request 50 at a time. I only requested the total of what I needed for the project (200 videos) and added a small delay between requests to avoid hitting limits or overwhelming the server.

---

