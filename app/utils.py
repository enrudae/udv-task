import json
from collections import defaultdict


def load_news():
    with open('data/news.json', 'r') as file:
        data = json.load(file)
    return [news for news in data['news'] if not news['deleted']]


def load_comments():
    with open('data/comments.json', 'r') as file:
        data = json.load(file)
    return data['comments']


def get_count_comments_by_news_id():
    count_comments_by_news_id = defaultdict(int)
    comments_list = load_comments()
    for comment in comments_list:
        count_comments_by_news_id[comment['news_id']] += 1
    return count_comments_by_news_id
