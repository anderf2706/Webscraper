#! python3
import pandas as pd
import praw
import datetime as dt

reddit = praw.Reddit(client_id='ZMYsLBXNwHSteQ',
                     client_secret='7ylJljQjBWxgZThkDp_dtW194pE',
                     user_agent='scraper',
                     username='anderf2706',
                     password='3280TjodalynG')

subreddit = reddit.subreddit('stocks')

top_subreddit = subreddit.new(limit=10)
for post in top_subreddit:
    print(post.title, "   :   ",post.id)