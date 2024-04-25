#!/usr/bin/python3
"""
Using first task extend your Python script to export data in the CSV format
"""
import csv
import json
import requests
import sys


def get_employee_data(user_id):
    """Fetches TODO list data and employee name from the API."""
    base_url = 'https://jsonplaceholder.typicode.com'
    user_response = requests.get(f"{base_url}/users/{user_id}")
    todos_response = requests.get(f"{base_url}/todos?userId={user_id}")

    # Check if requests were successful
    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Failed to fetch data from API")
        sys.exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    return todos_data, user_data['username']


def export_to_csv(todo_list, user_id, username):
    """Exports TODO list data to a CSV file."""
    filename = f"{user_id}.csv"

    with open(filename, "w", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in todo_list:
            writer.writerow([
                user_id,
                username,
                task.get('completed'),
                task.get('title')
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    todo_list, username = get_employee_data(user_id)
    export_to_csv(todo_list, user_id, username)
