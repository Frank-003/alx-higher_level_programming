#!/bin/bash
# Taking request of URL and display size of the body
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
