#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers"""

import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-agent": "MyApp/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data').get('children')
        for entry in data:
            print(entry.get('data').get('title'))
    else:
        print(None)
