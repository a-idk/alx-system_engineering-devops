#!/usr/bin/python3
"""
Title: Export to CSV
Description: Script that, using this REST API, for a given employee ID,
            returns information about his/her TODO list progress and
            also export data in the CSV format
@a_idk scripting
"""

import csv
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

    with open(f"{emp_id}.csv", "w", newline="") as csvfile:
        csv_write = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        head_row = ["User ID", "Username", "Completed", "Title"]
        # csv_write.writerow(head_row)
        for idx in todo_lst:
            csv_row = [emp_id, user_name, idx.get("completed"),
                    idx.get("title")]
            csv_write.writerow(csv_row)
