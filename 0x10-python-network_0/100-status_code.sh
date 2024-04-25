#!/bin/bash
# sends a request to a URL passed as an argument
curl -s -o /dev/null -I --w "%{http_code}" "$1"
