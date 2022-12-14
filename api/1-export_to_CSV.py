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

    file = open("{}.csv".format(user["id"]), "w")

    for task in tasks:
        file.write("\"{}\",\"{}\","
                   "\"{}\",\"{}\"\n".format(user["id"],
                                            user["username"],
                                            task["completed"],
                                            task["title"]))
    file.close()
