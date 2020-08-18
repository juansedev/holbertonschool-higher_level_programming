#!/bin/bash
# Script to get the Contentn-Lenght a throught curl command
curl -sI "$1" | grep "Allow:" | sed 's/Allow: //'
