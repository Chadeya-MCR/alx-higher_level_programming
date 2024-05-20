#!/bin/bash

# Function to display usage
usage() {
    echo "Usage: $0 URL"
}

# Check if the number of arguments is less than 1
if [ "$#" -lt 1 ]; then
    usage
    exit 1
fi

# Assign the argument to a variable
URL=$1

# Use curl to send a request to the URL and get the size of the response body
BODY_SIZE=$(curl -s -o /dev/null -w '%{size_download}' "$URL")

# Print the size of the body in bytes
echo "$BODY_SIZE"

