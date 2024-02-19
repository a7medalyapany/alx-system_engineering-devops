#!/usr/bin/python3
"""Fetches data from an API and exports it to a JSON file for a given employee ID."""

import json
import requests
import sys


def fetch_employee_todo_progress(employee_id):
    """Fetches data from an API and exports it to a JSON file for a given employee ID."""
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(url)
    todos = response.json()

    if not todos:
        print("No data found for the given employee ID.")
        return

    response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee_data = response.json()
    employee_name = employee_data.get('username')

    json_data = {employee_id: []}

    for todo in todos:
        json_data[employee_id].append({
            "task": todo['title'],
            "completed": todo['completed'],
            "username": employee_name
        })

    json_filename = f"{employee_id}.json"

    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    print(f"Data exported to {json_filename} successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)
