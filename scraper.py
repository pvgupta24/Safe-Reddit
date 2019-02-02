#! usr/bin/env python3
import praw
import pandas as pd
# import datetime as dt
from sys import argv
import os

reddit = praw.Reddit(
    client_id=os.environ['REDDIT_CLIENT_ID'],
    client_secret=os.environ['REDDIT_CLIENT_SECRET'],
    user_agent=os.environ['REDDIT_APP_NAME'],
    username=os.environ['REDDIT_USERNAME'],
    password=os.environ['REDDIT_PASSWORD']
)

subreddit = reddit.subreddit('all')
searchQuery = argv[1]

# topics_dict = {
#     'title': [], 'score': [], 'id': [],
#     'url': [], 'comms_num': [], 'created': [], 'body': []
#     }

topics_dict = { 'id': [], 'comment_text': [] }
topics = ['happy']

for topic in topics:
    for post in subreddit.search(topic, limit=100):
        # topics_dict['title'].append(post.title)
        # topics_dict['score'].append(post.score)
        topics_dict['id'].append(post.id)
        topics_dict['comment_text'].append(f'{post.title}\n{post.selftext}')
        # topics_dict['url'].append(post.url)
        # topics_dict['comms_num'].append(post.num_comments)
        # topics_dict['created'].append(post.created)
        # topics_dict['body'].append(post.selftext)

topics_data = pd.DataFrame(topics_dict)
topics_data.to_csv(f'{searchQuery}.csv', encoding='utf-8', index=False, quoting=1)

# print(topics_data.head(20))
