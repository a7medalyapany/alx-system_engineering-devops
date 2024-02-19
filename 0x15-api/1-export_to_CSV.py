#!/usr/bin/python3
"""Fetches data from an API and exports it to a CSV file for a given employee ID."""

import csv
import requests
import sys


def fetch_employee_todo_progress(employee_id):
    """Fetches data from an API and exports it to a CSV file for a given employee ID."""
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

    csv_filename = f"{employee_id}.csv"

    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['USER_ID', 'USERNAME',
                         'TASK_COMPLETED_STATUS', 'TASK_TITLE'])

        for todo in todos:
            writer.writerow([employee_id, employee_name,
                             todo['completed'], todo['title']])

    print(f"Data exported to {csv_filename} successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)
