#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles of the first 10
"""

import requests


def top_ten(subreddit):
    """
    return top 10
    """
    url = 'https://www.reddit.com/r/{}/hot/.json?limit=10'
    header = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                print(post['data']['title'])
    else:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
