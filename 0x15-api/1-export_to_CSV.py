#!/usr/bin/python3
"""Exports to-do list info for a given employee ID to CSV."""

import csv
import requests
import sys

if __name__ == "__main__":
    # Get user ID from command-line args
    user_id = sys.argv[1]

    # Base URL for JSON API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user info from API
    user = requests.get(url + "users/{}".format(user_id)).json()

    # Extract username
    username = user.get("username")

    # Fetch to-do list items for user ID
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Write to-do list details to CSV
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
        ) for t in todos]
