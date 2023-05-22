#!/bin/bash

userName="nuts"
passWord="0424ds"
auth="mschap"

curl -X POST -d "ID=$userName&PW=$passWord&AUTH=$auth" http://localhost:5000/API/mainAPI