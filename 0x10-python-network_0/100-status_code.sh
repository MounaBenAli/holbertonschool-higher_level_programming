#!/bin/bash
#This script  sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -sLI "$1" --output /dev/null --write-out '%{http_code}'
