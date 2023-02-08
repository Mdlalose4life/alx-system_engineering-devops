#!/usr/bin/python3
"""
Script to export the imployees information to a JSON file.
"""

import requests
import json
import sys

if __name__ == '__main__':
    ID = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users" + "/" + ID

"""Getting the username from api"""
response = requests.get(url)
username = response.json().get('username')

"""Getting the todos of the employees from api"""
response = requests.get(url + "/todos")
tasks = response.json()

"""Making a dictionary of the employees and todos"""
dictionary = {ID: []}
for task in tasks:
    dictionary[ID].append({
        "todo": task.get('title'),
        "completed": task.get('completed'),
        "username": username
    })

"""Exporting the dictionary to a JSON file"""
with open('{}.json'.format(ID), 'w') as f:
    json.dump(dictionary, f)
