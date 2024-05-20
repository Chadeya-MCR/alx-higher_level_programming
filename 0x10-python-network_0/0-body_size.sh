#!/bin/bash
# Sends a request to the given URL and displays the size of the response body in bytes
[ "$#" -lt 1 ] && exit 1; curl -s -o /dev/null -w '%{size_download}\n' "$1"
