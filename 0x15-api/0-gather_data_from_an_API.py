#!/usr/bin/python3
"""
Title: Gathering data from an API
Description: Script that, using this REST API, for a given employee ID,
            returns information about his/her TODO list progress
@a_idk scripting
"""

import requests
import sys


if __name__ == "__main__":
    # setting the url, parameters and variables as given
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = sys.argv[1]
    us_data = requests.get(url + f"users/{emp_id}").json()
    todo_lst = requests.get(url + "todos", {"userId": emp_id}).json()

    comp_task = []
    for idx in todo_lst:
        if idx.get("completed") is True:
            comp_task.append(idx.get("title"))

    # printing the first line
    print(
            'Employee {} is done with tasks({}/{}):'.format(
                us_data.get("name"),
                len(comp_task),
                len(todo_lst)
                )
    """
    print(
            f"Employee {us_data.get('name')} is done with tasks"
            f"({len(comp_task)}/{len(todo_lst)}):"
            )

    print(f"Employee {user.get('name')} is done with
    task({len(comp_task)}/{len(todo_lst)})")
    print("Employee {} is done with tasks({}/{}):".format(user.get("name"),
        len(comp_task), len(todo_lst)))
    """

    # printing the second line
    for idx in comp_task:
        print(f"\t{idx}")
