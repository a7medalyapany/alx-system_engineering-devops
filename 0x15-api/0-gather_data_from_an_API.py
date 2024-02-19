#!/usr/bin/python3
"""Fetches data from an API and displays it for a given employee ID."""

import requests
import sys


def fetch_employee_todo_progress(employee_id):
    """Fetches data from an API and displays it for a given employee ID."""
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(url)
    todos = response.json()

    if not todos:
        print("No data found for the given employee ID.")
        return

    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo['completed'])

    response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee_data = response.json()
    employee_name = employee_data.get('name')

    print(
        f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    for todo in todos:
        if todo['completed']:
            print(f"\t{todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)
