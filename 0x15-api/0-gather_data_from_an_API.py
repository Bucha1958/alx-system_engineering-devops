#!/usr/bin/python3
"""
    A python script that uses REST API that returns 
    information about an employees' 
    TODO list based on his/her ID information
"""
import requests
from sys import argv


def get_todo_progress(employee_id):
    rest_api_url = "https://jsonplaceholder.typicode.com"
    url = "{}/todos?userId={}".format(rest_api_url, employee_id)
    response = requests.get(url)

    if response.status_code == 200:
        todo_list = response.json()
        user_url = "{}/users/{}".format(rest_api_url, employee_id)
        user_response = requests.get(user_url)
        if user_response.status_code == 200:
            get_json = user_response.json()
            employee_name = get_json.get("name")
        number_tasks = len(todo_list)
        task_completed = 0
        task_list = ""
        
        for task in todo_list:
            if task.get("completed") is True:
                task_completed += 1
                task_list += "\t " + task.get("title") + "\n"
        
        print("Employee {} is done with tasks({}/{})".format(employee_name,
            task_completed, number_tasks))
        print(task_list[:-1])


if __name__ == "__main__":
    get_todo_progress(argv[1])
