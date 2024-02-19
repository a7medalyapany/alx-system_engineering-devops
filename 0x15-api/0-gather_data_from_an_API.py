#!/usr/bin/python3
"""
Gets to-do list info for an employee ID.

This script fetches user info and to-dos from JSONPlaceholder API
for the given employee ID. Prints completed tasks by the employee.
"""

import requests
import sys

if __name__ == "__main__":
    # Base URL for JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Get employee info using provided ID
    employee_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employee_id)).json()

    # Get to-do list for employee using provided ID
    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params).json()

    # Filter and count completed tasks
    completed = [t.get("title") for t in todos if t.get("completed")]

    # Print employee's name and number of completed tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Print completed tasks with indentation
    for task in completed:
        print("\t {}".format(task))
