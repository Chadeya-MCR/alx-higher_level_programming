#!/bin/bash
#script sends a PUT request to 0.0.0.0:5000/catch_me to receive a response with "You got me!" in the body
curl -sL -X PUT -d "user_id=98" -H "Origin: School" 0.0.0.0:5000/catch_me
