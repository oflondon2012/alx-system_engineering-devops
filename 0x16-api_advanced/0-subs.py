#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subs
"""

import requests


def number_of_subscribers(subreddit):
    """ return the number of subcribers for a given subreddit """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
