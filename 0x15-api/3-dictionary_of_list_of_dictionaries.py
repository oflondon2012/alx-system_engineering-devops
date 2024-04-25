#!/usr/bin/python3
"""
 extend your Python script to export data in the JSON format.
"""
import json
import requests
import sys


def fetch_todo_data():
    """Fetches user data and TODO list for a given user ID."""
    user_response = requests.get("https://jsonplaceholder.typicode.com/users")
    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')

    # Fetch user data
    user_data = user_response.json()

    # Fetch TODO list
    todos_data = todos_response.json()

    # Filter tasks for the specific user
    todos = {}
    for user in user_data:
        tasks = []
        for task in todos_data:
            if task.get('userId') == user.get('id'):
                task_dict = {
                    "username": user.get('username'),
                    "task": task.get('title'),
                    "completed": task.get('completed')
                }
            tasks.append(task_dict)
        todos[user.get('id')] = tasks

    return todos


def save_todo_data():
    """Saves user tasks to a JSON file."""
    todos = fetch_todo_data()

    with open('todo_all_employees.json', mode='w') as file:
        json.dump(todos, file)


if __name__ == "__main__":
    save_todo_data()
