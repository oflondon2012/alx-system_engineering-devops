#!/usr/bin/python3
"""
script fetches information about a user's TODO list progress using a REST API.
"""

import json
import requests
import sys


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


def count_completed_tasks(todo_list):
    """Counts the number of completed tasks in the TODO list."""
    completed_tasks = [task for task in todo_list if task['completed']]
    return completed_tasks


def print_task_progress(employee_name, total_tasks, completed_tasks):
    """Prints the progress of the employee's TODO list."""
    print("Employee {} is done with tasks ({}/{}):"
          .format(employee_name, len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print("\t{}".format(task['title']))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    todo_list, employee_name = get_employee_data(employee_id)
    total_tasks = len(todo_list)
    completed_tasks = count_completed_tasks(todo_list)
    print_task_progress(employee_name, total_tasks, completed_tasks)
