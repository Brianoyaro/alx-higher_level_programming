#!/bin/bash
#post using json
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
