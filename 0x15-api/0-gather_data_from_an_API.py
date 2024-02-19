#!/usr/bin/python3
"""Fetches data from an API and displays it for a given employee ID."""

import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(base_url, params={"userId": employee_id})

    if response.status_code != 200:
        print("Error: Unable to fetch data from the API")
        return

    todos = response.json()
    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo['completed']]
    num_completed_tasks = len(completed_tasks)
    employee_name = todos[0]['name'] if todos else "Unknown"

    print(
        f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
    for todo in todos:
        print(f"\t{todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
