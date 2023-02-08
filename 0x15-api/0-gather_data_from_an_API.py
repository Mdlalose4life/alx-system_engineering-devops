#!/usr/bin/python3
""" Python script that uses REST API for given employee ID, returns
information about the emplyee's TODO list progress"""

import requests
import sys

if '__name__' == '__main__':
    ID = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users" + "/" + ID

    """Getting the name of the employee"""
    response = requests.get(url)
    employee_Name = response.json().get('name')

    """Getting the todo list of the employee"""
    response = requests.get(url + "/todos")
    employee_TodoList = response.json().get('items')
    complete = 0
    complete_task = []

    """Getting the list of completed tasks of the employees"""
    for task in employee_TodoList:
        if task.get('completed'):
            complete += 1
            complete_task.append(employee_TodoList)

    """Printing the information about the employees"""
    print("Employee {} is done with tasks({}/{}):"
        .format(employee_Name, complete, len(employee_TodoList)))

    """Printing the list of completed tasks of the employees"""
    for task in complete_task:
        print("\t {}".format(task.get('title')))
