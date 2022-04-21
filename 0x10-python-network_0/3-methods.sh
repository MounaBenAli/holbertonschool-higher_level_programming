#!/bin/bash
#This script takes in a URL & displays all HTTP methods the server will accept.
curl -i -X OPTIONS "$1"