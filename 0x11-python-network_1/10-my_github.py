#!/usr/bin/python3
"""displays id of an authenticated github user"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    name = sys.argv[1]
    pwd = sys.argv[2]
    r = requests.get(url, auth=(name, pwd))
    print(r.json().get('id'))
