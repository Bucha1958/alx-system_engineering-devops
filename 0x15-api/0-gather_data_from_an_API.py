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
            EMPLOYEE_NAME = get_json.get("name")
        TOTAL_NUMBER_OF_TASKS = len(todo_list)
        NUMBER_OF_DONE_TASKS = 0
        TASK_TITLE = ""
        
        for task in todo_list:
            if task.get("completed") is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE += "\t " + task.get("title") + "\n"
        
        print("Employee {} is done with tasks({}/{})".format(EMPLOYEE_NAME,
            NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
        print(task_list[:-1])


if __name__ == "__main__":
    get_todo_progress(argv[1])
