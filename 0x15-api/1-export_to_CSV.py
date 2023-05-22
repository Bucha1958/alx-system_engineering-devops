#!/usr/bin/python3
"""
    A python script that uses REST API, the users' output 
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
    
    file_name = "{}.csv".format(employee_id)

    with open(file_name, "a") as fd:
        for todo in todo_list:
            completed = todo.get("completed")
            title = todo.get("title")
            csv_data = "\"{}\",\"{}\",\"{}\",\"{}\"\n".format(
                    employee_id, employee_name,completed,title
                    )
            fd.write(csv_data)

if __name__ == "__main__":
    get_todo_progress(argv[1])
