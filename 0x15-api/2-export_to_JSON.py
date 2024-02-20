#!/usr/bin/python3
"""
Title: Export to JSON
Description: Script that, using this REST API, for a given employee ID,
            returns information about his/her TODO list progress and
            also export data in the JSON format
@a_idk scripting
"""

# import csv
import json
import requests
import sys


if __name__ == "__main__":
    # setting the url, parameters and variables as given
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = sys.argv[1]
    us_data = requests.get(url + f"users/{emp_id}").json()
    # username extraction
    user_name = us_data.get("username")
    # getting the todo list
    todo_lst = requests.get(url + "todos", {"userId": emp_id}).json()

    with open(f"{emp_id}.json", "w") as jsonfile:
        json_data = {emp_id: []}

        for tsk in todo_lst:
            tsk_dict = {
                    "task": tsk.get("title"),
                    "completed": tsk.get("completed"),
                    "username": user_name
                    }
            json_data[emp_id].append(tsk_dict)

        json.dump(json_data, jsonfile)
