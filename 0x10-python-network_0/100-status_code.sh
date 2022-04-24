#!/bin/bash
#This script  sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -L --output /dev/null --write-out "%{http_code}\n" --silent "$1"
