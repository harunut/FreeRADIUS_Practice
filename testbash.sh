#!/bin/bash

userName="nuts"
passWord="0424"
auth="chap"

curl -X POST -d "ID=$userName&PW=$passWord&AUTH=$auth" http://localhost:5000/API/mainAPI