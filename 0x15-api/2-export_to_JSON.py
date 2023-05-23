#!/usr/bin/python3
"""
    A python script that uses REST API, the users' output 
"""
import json
import requests
from sys import argv


def get_todo_progress(employee_id):
    rest_api_url = "https://jsonplaceholder.typicode.com"
    url = "{}/users/{}/todos".format(rest_api_url, employee_id)
    response = requests.get(url)
    todo_list = response.json()

    user_url = "{}/users/{}".format(rest_api_url, employee_id)
    user_response = requests.get(user_url)
    get_json = user_response.json()
    employee_name = get_json.get("name")

    task_list = []
    
    for task in todo_list:
        task_dict = {}
        task_dict["task"] = task.get("title")
        task_dict["completed"] = task.get("completed")
        task_dict["username"] = employee_name
        task_list.append(task_dict)

    todos = {"{}".format(employee_id): task_list}

    file_name = "{}.json".format(employee_id)
    with open(file_name, "w") as fd:
        json.dump(todo_list, fd)

if __name__ == "__main__":
    get_todo_progress(argv[1])
