#!/usr/bin/python3
"""
Using first task extend your Python script to export data in the CSV format
"""

import json
import requests
import sys
import csv


def get_employee_data(employee_id):
    """Fetches TODO list data and employee name from the API."""
    base_url = 'https://jsonplaceholder.typicode.com/users/{}'
    todos_url = base_url + '/todos'
    name_url = base_url.format(employee_id)

    # Get TODO list and employee name
    with requests.Session() as session:
        todo_res = session.get(todos_url.format(employee_id))
        name_res = session.get(name_url)

    # Check if requests were successful
    if todo_res.status_code != 200 or name_res.status_code != 200:
        print("Failed to fetch data from API")
        sys.exit(1)

    return todo_res.json(), name_res.json()['name']


def export_to_csv(todo_list, employee_id, username):
    """Exports TODO list data to a CSV file."""
    filename = f"{employee_id}.csv"

    with open(filename, "w", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in todo_list:
            writer.writerow([
                employee_id,
                username,
                task.get('completed'),
                task.get('title')
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    todo_list, username = get_employee_data(employee_id)
    export_to_csv(todo_list, employee_id, username)
