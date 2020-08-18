#!/bin/bash
# Script to get the Contentn-Lenght a throught curl command
curl -o /dev/null -s -w "%{http_code}" "$1"
