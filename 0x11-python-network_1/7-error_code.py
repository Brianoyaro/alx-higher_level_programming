#!/usr/bin/python3
"""handles request response errors"""
import sys
import requests


if __name__ == "__main__":
    body = requests.get(sys.argv[1])
    if body.status_code >= 400:
        print("Error code: {}".format(body.status_code))
    else:
        print(body.text)
