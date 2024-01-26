#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the passed URL"""
import sys
import requests


if __name__ == "__main__":
    value = {"email": sys.argv[2]}
    body = requests.post(sys.argv[1], value)
    print(body.text)
