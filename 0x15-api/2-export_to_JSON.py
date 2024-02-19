#!/usr/bin/python3
"""
Exports to-do list info for a given employee ID to JSON format.

This script exports user info and to-do list to a JSON file.
"""

import json
import requests
import sys

if __name__ == "__main__":
    # Get employee ID from command-line arg
    user_id = sys.argv[1]

    # Base URL for JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user info
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    # Fetch to-do list for employee ID
    params = {"userId": user_id}
    todos = requests.get(url + "todos", params).json()

    # Create dictionary with user and to-do list info
    data_to_export = {
        user_id: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            }
            for t in todos
        ]
    }

    # Write data to JSON file
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
