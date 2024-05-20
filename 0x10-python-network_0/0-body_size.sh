#!/bin/bash
#sript that displays the size of the body of the response
[ "$#" -lt 1 ] && exit 1
curl -s -o /dev/null -w '%{size_download}\n' "$1"

