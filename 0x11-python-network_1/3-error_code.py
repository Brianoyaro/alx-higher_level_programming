#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays the body"""
import urllib.request
import sys


if __name__ == "__main__":
    try:
        urllib.request.urlopen(sys.argv[1])
    except urllib.error.HTTPError as e:
        print(e.code)
    else:
        with urllib.request.urlopen(sys.argv[1]) as response:
            body = response.read()
            print(body.decode('utf8'))
