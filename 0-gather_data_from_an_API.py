#!/usr/bin/python3
"""
Write a Python script that, for a given employee ID,
returns information about his/her TODO list progress.
"""

import urllib.request
import sys
import json

request_url = urllib.request.urlopen('https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
response = request_url.read()
user = json.loads(response.decode('utf-8'))

request_url = urllib.request.urlopen('https://jsonplaceholder.typicode.com/todos?userId={}'.format(sys.argv[1]))
response = request_url.read()
todos = json.loads(response.decode('utf-8'))

done_tasks = list(filter(lambda todo: todo['completed'], todos))
print("Employee {} is done with tasks({}/{}):".format(user['name'], len(done_tasks), len(todos)))
for todo in done_tasks:
    print("\t{}".format(todo['title']))
