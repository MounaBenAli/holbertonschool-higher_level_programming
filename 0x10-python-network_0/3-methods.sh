#!/bin/bash
#This script takes in a URL & displays all HTTP methods the server will accept.
curl -sI "$1" | grep "Allow" | cut -d' ' -f 2-
