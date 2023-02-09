#!/usr/bin/python3
"""
Dictionary Represation of the todo list of the employees.
"""

import requests
import json
import sys

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
users = response.json()

dictionary = {ID: []}
for task in users:
    user_id = user.ger('id')
    username = user.get('username')
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_is)
    url = url + 'todos/'
    response = requests.get(url)
    tasks = response.json()
    dictionary[user_id] = []
    for task in tasks:
        dictionary[user_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
            })

"""Exporting the dictionary to a JSON file"""
with open('todo_all_employees.json', 'w') as f:
    json.dump(dictionary, f)
