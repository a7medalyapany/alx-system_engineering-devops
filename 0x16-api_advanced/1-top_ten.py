#!/usr/bin/python3
"""
Module to fetch and print the titles of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Function to retrieve and print the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit: A string representing the name of the subreddit.

    Returns:
        None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        'User-Agent': 'python3:subreddit.subscriber.counter:v1.0 (by /user/alyapany)'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
