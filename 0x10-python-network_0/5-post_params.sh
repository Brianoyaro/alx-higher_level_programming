#!/bin/bash
# curl post together with parameters
curl -s -X POST -L -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
