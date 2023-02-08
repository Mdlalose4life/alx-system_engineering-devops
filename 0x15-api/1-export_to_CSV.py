#!/usr/bin/python3
"""
Script to export the imployees information to a CSV file.
"""

import requests
import sys

if __name__ == '__main__':
    ID = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users" + "/" + ID

    """gettint usernames of the emplyees"""
    response = requests.get(url)
    username = response.json().get('username')

    """getting the todo list of the employees from the API"""
    response = requests.get(url + "/todos")
    todos = response.json()

    """Writing the todo list to a CSV file"""
    with open('{}.csv'.format(ID), 'w') as f:
        for task in todos:
            f.write('"{}","{}","{}","{}"\n'
                    .format(ID, username, task.get('completed'),
                            task.get('title')))
