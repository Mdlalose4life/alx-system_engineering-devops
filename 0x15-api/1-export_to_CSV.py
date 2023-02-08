#!/usr/bin/python3
"""
Script to export the imployees information to a CSV file.
"""

import requests
import sys

if __name__ == '__main__':
    ID = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users" + "/" + ID

    response = requests.get(url)
    username = response.json().get('username')

    response = requests.get(url + "/todos")
    todos = response.json()

    with open('{}.csv'.format(ID), 'w') as f:
        for task in todos:
            f.write('"{}","{}","{}","{}"\n'
                    .format(ID, username, task.get('completed'),
                            task.get('title')))
