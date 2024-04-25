#!/usr/bin/python3
"""
 extend your Python script to export data in the JSON format.
"""
import json
import requests
import sys


def fetch_user_data(user_id):
    """Fetches user data and TODO list for a given user ID."""
    url_str = 'https://jsonplaceholder.typicode.com/users/{}'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    # Fetch user data
    user_response = requests.get(url_str.format(user_id))
    user_data = user_response.json()

    # Fetch TODO list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Filter tasks for the specific user
    user_tasks = []
    for task in todos_data:
        if task.get('userId') == int(user_id):
            task_dict = {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": user_data.get('username')
            }
            user_tasks.append(task_dict)

    return user_tasks


def save_user_tasks(user_id):
    """Saves user tasks to a JSON file."""
    tasks = fetch_user_data(user_id)
    user_data = {user_id: tasks}
    file_name = f"{user_id}.json"

    with open(file_name, mode="w") as user_file:
        json.dump(user_data, user_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python module.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    save_user_tasks(user_id)
