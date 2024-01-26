#!/usr/bin/python3
"""handles request response errors"""
import sys
import requests


if __name__ == "__main__":
    try:
        response = requests.get(sys.argv[1])
        print(response.text)
    except requests.exceptions as e:
        if e.status_code >= 400:
            print("Error code:" e.status_code)
