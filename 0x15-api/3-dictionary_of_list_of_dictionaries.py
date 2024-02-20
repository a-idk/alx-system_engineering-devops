#!/usr/bin/python3
"""
Title: Dictionary of list of dictionaries
Description: Script that, using this REST API, for a given employee ID,
            returns information about his/her TODO list progress and
            also export data in the JSON format
@a_idk scripting
"""

# import csv
import json
import requests
# import sys


if __name__ == "__main__":
    # setting the url, parameters and variables as given
    url = "https://jsonplaceholder.typicode.com/"
    # emp_id = sys.argv[1]
    # us_data = requests.get(url + f"users/{emp_id}").json()
    us_data = requests.get(url + "users").json()
    # username extraction
    # user_name = us_data.get("username")
    # getting the todo list
    # todo_lst = requests.get(url + "todos", {"userId": emp_id}).json()

    with open("todo_all_employees.json", "w") as jsonfile:
        all_tsk = {}

        # iterating over user
        for x in us_data:
            emp_id = x.get("id")
            username = x.get("username")
            user_tsk = requests.get(
                    url + "todos", params={"userId": emp_id}
                    ).json()
            user_tsk_lst = []
            # Iterating over each task in the tasks list
            for tsk in user_tsk:
                tsk_dict = {
                        "task": tsk.get("title"),
                        "completed": tsk.get("completed"),
                        "username": username
                        }
                user_tsk_lst.append(tsk_dict)
            # Assigning the list of tasks for this user to the user's
            # id in the dictionary
            all_tsk[emp_id] = user_tsk_lst  

        json.dump(all_tsk, jsonfile)  #JSON data to the file
