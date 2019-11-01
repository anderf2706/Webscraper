#! python3
import pandas as pd
import praw
import datetime as dt

def gather_data(amount):
    reddit = praw.Reddit(client_id='ZMYsLBXNwHSteQ',
                         client_secret='7ylJljQjBWxgZThkDp_dtW194pE',
                         user_agent='scraper',
                         username='anderf2706',
                         password='3280TjodalynG')

    subreddit = reddit.subreddit('stocks')

    subreddits= subreddit.search(,limit=amount)
    for post in subreddits:
        print(post.title, "   :   ", post.id)