#!/bin/bash
# Script to get the Contentn-Lenght a throught curl command
curl -Is "$1" | grep Content-Length | cut -d " " -f2
