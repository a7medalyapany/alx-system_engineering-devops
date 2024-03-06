#!/usr/bin/python3
"""
Module to fetch and return a list containing titles
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function to retrieve and return list of title
    Args:
        subreddit: A string representing the name.
        hot_list: A list to store the titles.
        after: A string representing the "after" parameter.

    Returns:
        A list containing the titles of all hot articles
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {
        'User-Agent':
        'python3:subreddit.subscriber.counter:v1.0 (by /user/alyapany)'}
    params = {"after": after} if after else {}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            print(len(result))
        else:
            print("None")
