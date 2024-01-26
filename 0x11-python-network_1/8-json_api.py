#!/usr/bin/python3
"""searches using given parameter"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 1:
        value = {q: ""}
    else:
        value = {q: sys.argv[1]}
    response = requests.post(url, value)
    if 'application/json' in response.headers.get('Content-Type', ''):
        if response.text:
            print("[{}] {}".format(response.get('id'), response.get('name')))
        else:
            print("No result")
    else:
        print("Not a valid JSON")
