#!/usr/bin/python3
"""
    A python script that uses REST API
"""
import requests
from sys import argv


def get_todo_progress(employee_id):
    rest_api_url = "https://jsonplaceholder.typicode.com"
    url = "{}/todos?userId={}".format(rest_api_url, employee_id)
    response = requests.get(url)
    todo_list = response.json()
    number_tasks = len(todo_list)

    user_url = "{}/users/{}".format(rest_api_url, employee_id)
    user_response = requests.get(user_url)
    get_json = user_response.json()
    employee_name = get_json.get("name")

    number_of_done_tasks = 0
    task_title = ""
    for task in todo_list:
        if task.get("completed") is True:
            number_of_done_tasks += 1
            task_title += "\t " + task.get("title") + "\n"
    print(f"Employee {employee_name} is done with tasks 
            ({number_of_done_tasks}/{number_tasks})")
    print(task_title[:-1])


if __name__ == "__main__":
    get_todo_progress(argv[1])
