    #! usr/bin/env python3
import praw
import pandas as pd
import model_output
# import datetime as dt
# from sys import argv
import os

def scrape_file(input_query):
    reddit = praw.Reddit(
        client_id=os.environ['REDDIT_CLIENT_ID'],
        client_secret=os.environ['REDDIT_CLIENT_SECRET'],
        user_agent=os.environ['REDDIT_APP_NAME'],
        username=os.environ['REDDIT_USERNAME'],
        password=os.environ['REDDIT_PASSWORD']
    )

    subreddit = reddit.subreddit('all')
    searchLimit = 10
    # searchQuery = input_query

    # topics_dict = {
    #     'title': [], 'score': [], 'id': [],
    #     'url': [], 'comms_num': [], 'created': [], 'body': []
    #     }

    topics_dict = { 'id': [], 'comment_text': [] }
    topics = [input_query]

    for topic in topics:
        for post in subreddit.search(topic, limit=searchLimit):
            # topics_dict['title'].append(post.title)
            # topics_dict['score'].append(post.score)
            topics_dict['id'].append(post.id)
            topics_dict['comment_text'].append(f'{post.title}\n{post.selftext}')
            # topics_dict['url'].append(post.url)
            # topics_dict['comms_num'].append(post.num_comments)
            # topics_dict['created'].append(post.created)
            # topics_dict['body'].append(post.selftext)

    topics_data = pd.DataFrame(topics_dict)
    # topics_data.to_csv(f'{searchQuery}.csv', encoding='utf-8', index=False, quoting=1)
    # model_output.predict_output(searchQuery+'.csv')
    censored_ids = model_output.predict_output(topics_data)
    censored_posts = []
    
    print('anuzenith29')
    for i in censored_ids:
        print(i)
        sub = reddit.submission(i)
        censored_posts.append(sub)

    return censored_posts
# print(topics_data.head(20))

