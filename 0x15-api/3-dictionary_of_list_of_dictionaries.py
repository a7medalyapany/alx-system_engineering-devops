#!/usr/bin/python3
"""Fetches data from an API and exports it to a JSON file for all employee IDs."""

import json
import requests
from sys import argv


def fetch_data_and_export_to_json():
    """Fetches data from an API and exports it to a JSON file for all employee IDs."""
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    tasks = response.json()

    """ Create a dictionary to store tasks for each user """
    tasks_by_user = {}

    for task in tasks:
        """ Extract relevant task information """
        user_id = task.get("userId")
        task_info = {
            "username": task.get("username"),
            "task": task.get("title"),
            "completed": task.get("completed")
        }

        """ Check if user ID already exists in dictionary """
        if user_id in tasks_by_user:
            tasks_by_user[user_id].append(task_info)
        else:
            tasks_by_user[user_id] = [task_info]

    """ Export data to JSON file """
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(tasks_by_user, json_file)


if __name__ == "__main__":
    fetch_data_and_export_to_json()
