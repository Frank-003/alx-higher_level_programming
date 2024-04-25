#!/bin/bash
# Taking request of URL and display size of the body

if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

response=$(curl -s -o response_body.tmp -w "%{size_download}" "$url")

echo "Size of the response body: $response bytes"

rm response_body.tmp
