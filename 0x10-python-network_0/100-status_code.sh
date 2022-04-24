#!/bin/bash
#This script  sends a request to a URL passed as an argument, and displays only the status code of the response.
curl --write-out "%{http_code}\n" --silent --output /dev/null "$1"