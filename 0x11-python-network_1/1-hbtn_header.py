#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""
import urllib.request
import sys


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        pass
    print(response.headers.get("X-Request-Id"))
