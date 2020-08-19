#!/bin/bash
# Script to get the http_code a throught curl command
curl -o /dev/null -s -w "%{http_code}" "$1"
