#!/usr/bin/python3
"""
This module retrieves the number of subscribers for a subreddit from Reddit API.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for a given subreddit.

    Args:
        subreddit: A string representing the subreddit name.

    Returns:
        The number of subscribers of the subreddit. If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "alyapany"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            return data.get('subscribers', 0)
    return 0


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subscribers = number_of_subscribers(sys.argv[1])
        print("{:d}".format(subscribers))
