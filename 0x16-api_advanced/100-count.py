#!/usr/bin/python3
"""
Module to fetch and print a sorted count of given keywords in the titles
 of all hot articles
for a given subreddit using recursion.
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursive function to count the occurrences of given keywords
        in the titles of all hot articles 
        for a given subreddit.

    Args:
        subreddit: A string representing the name of the subreddit.
        word_list: A list of keywords to count occurrences of.
        after: A string representing the "after" parameter for pagination.
        counts: A dictionary to store the counts of each keyword.

    Returns:
        None.
    """
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {
        'User-Agent': 'python3:subreddit.subscriber.counter:v1.0 (by /user/alyapany)'}
    params = {"after": after} if after else {}
    response = requests.get(url, headers=headers, params=params)

    # Check if the subreddit exists
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if word.lower() in title:
                    counts[word.lower()] = counts.get(word.lower(), 0) + 1
        after = data['data']['after']
        if after:
            return count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        return None


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(
            sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        keywords = sys.argv[2].split()
        count_words(subreddit, keywords)
