#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the passed URL"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf8'))
