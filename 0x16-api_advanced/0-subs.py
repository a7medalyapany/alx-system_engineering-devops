#!/usr/bin/python3
"""
Module to fetch the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function to retrieve the number of subscribers for a given subreddit.

    Args:
        subreddit: A string representing the name of the subreddit.

    Returns:
        The number of subscribers for the given subreddit, or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'python3:subreddit.subscriber.counter:v1.0 (by /user/alyapany)'}
    response = requests.get(url, headers=headers)

    # Check if the subreddit exists
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        print(number_of_subscribers(subreddit))
