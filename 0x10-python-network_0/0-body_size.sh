#!/bin/bash
#This script takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -L --output /dev/null --write-out "%{size_download}\n" --silent "$1"
