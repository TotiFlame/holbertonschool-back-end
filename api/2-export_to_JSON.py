#!/usr/bin/python3
"""
Write a Python script that, for a given employee ID,
returns information about his/her TODO list progress.
"""


if __name__ == "__main__":
    import json
    import sys
    import urllib.request

    request_url = urllib.request.urlopen("https://jsonplaceholder.typicode."
                                         "com/users/{}".format(sys.argv[1]))
    response = request_url.read()
    user = json.loads(response.decode("utf-8"))

    request_url = urllib.request.urlopen("https://jsonplaceholder.typicode.com"
                                         "/todos?userId={}"
                                         .format(sys.argv[1]))
    response = request_url.read()
    tasks = json.loads(response.decode("utf-8"))

    file = open("{}.json".format(user["id"]), "w")

    id = "{}".format(user["id"])

    userj = {id: []}

    for task in tasks:
        userj[id].append({
            "task": task["title"],
            "completed": task["completed"],
            "username": user["username"]
        })

    file.write(json.dumps(userj))
    file.close()
