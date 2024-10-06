#!/bin/bash

# Directory path
directory_path="./open-api-files"

# File name within the directory
file_name="open-api.yaml"

# Check if the directory exists
if [[ ! -d "$directory_path" ]]; then
    echo "Directory '$directory_path' does not exist."
    exit 1
fi

# Check if the file exists within the directory
if [[ ! -f "$directory_path/$file_name" ]]; then
    echo "File '$file_name' does not exist in directory '$directory_path'."
    exit 1
fi

if [[ -d "./openapi" ]]; then
    rm -rf openapi
fi

echo "Generating PY client for openapi"

yes | npx @openapitools/openapi-generator-cli generate -g python --additional-properties=prependFormOrBodyParameters=true,disallowAdditionalPropertiesIfNotPresent=false,generateSourceCodeOnly=true,packageName=openapi -o . -i ./open-api-files/open-api.yaml
rm -rf openapi/test
rm -rf openapi/README.md
rm -rf openapi/git_push.sh
rm -rf openapi/.travis
rm -rf openapi/.openapi-generator
rm -rf openapi/docs

echo "Generated PY client for openapi"
