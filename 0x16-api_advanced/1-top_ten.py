#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles of the first 10
"""

import requests


def top_ten(subreddit):
    """
    return top 10
    """
    url = 'https://www.reddit.com'
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.get('{}/r/{}/hot/.json?sort={}&limit={}'.format(
        url, subreddit, 'top', 10),
        headers=headers,
        allow_redirects=False)
    if response.status_code == 200:
        for post in response.json()['data']['children'][0:10]:
            print(post['data']['title'])
    else:
        print(None)
