#!/bin/bash
# setup_workspace.sh
#
# Purpose: Generation of API client for the Rapid7 Nexpose and InsightVM v3 API. Current supported languages: Python, Ruby, Go
#
# Requirements: Java install and on PATH
#
# Usage:
#  $ ./setup_workspace.sh param1
# * param1: Language for which to generate library (python, ruby, go)
# * param2: IP or hostname of console where Swagger spec is fetched
#
# Output: Generation of API and models based on Rapid7 Nexpose and InsightVM Swagger file

# Download InsightVM/Nexpose Console Version and update package in config.json
VERSION_URL="http://download2.rapid7.com/download/InsightVM/Rapid7Setup-Linux64.bin.version"
CONSOLE_VERSION=$(curl $VERSION_URL)
LIB_VERSION="1.0.0-$CONSOLE_VERSION"
sed -i '' "s/\"packageVersion\": \".*\"/\"packageVersion\": \"$LIB_VERSION\"/g" ./setup_workspace/config.json
echo "Library Version: $LIB_VERSION"


# Environment variable for branch name
echo 'LIB_VERSION='$LIB_VERSION > /var/jenkins_home/propsfile

# Download swagger file
API_FILE_DIR="api-files/"
SWAGGER_FILE=$API_FILE_DIR"console-swagger.json"
#SWAGGER_URL="https://help.rapid7.com/insightvm/en-us/api/api.json"
SWAGGER_URL="https://$2:3780/api/3/json"
wget --no-check-certificate $SWAGGER_URL -O $SWAGGER_FILE

# Manage swagger codegen
CODEGEN_JAR_NAME="swagger-codegen-cli"
CODEGEN_JAR_VERSION="2.4.0"
URL="http://central.maven.org/maven2/io/swagger/$CODEGEN_JAR_NAME/$CODEGEN_JAR_VERSION/$CODEGEN_JAR_NAME-$CODEGEN_JAR_VERSION.jar"
JAR_PATH="setup_workspace/$CODEGEN_JAR_NAME-$CODEGEN_JAR_VERSION.jar"

# Download and save codegen jar file
wget $URL -O $JAR_PATH

# Generate Library
CODEGEN_JAR="setup_workspace/$CODEGEN_JAR_NAME-$CODEGEN_JAR_VERSION.jar"

# Check if changes were made - new console version | new swagger file
if [[ `git status --porcelain --untracked-files=no` ]]; then
  # Changes
  echo "Changes detected, generating Library..."
  java -jar $CODEGEN_JAR generate -i $SWAGGER_FILE -l $1 \
       --git-user-id "rapid7" \
       --git-repo-id "vm-console-client-$1" \
       --release-note "Update generated library to version: $LIB_VERSION" \
       -o ./ -c setup_workspace/config.json
else
  # No changes
  echo 'No changes were made to client'
fi

if [ "$1" = "python" ]; then
  # Cleanup API documentation strings
  LC_ALL=C find . -type f -exec perl -0777 -i -pe 's/InsightVM API[\s]*# Overview.*/Python InsightVM API Client/' {} +
fi

if [ "$1" = "ruby" ]; then
  # Cleanup API documentation strings
  LC_ALL=C find . -type f -exec perl -0777 -i -pe 's/#InsightVM API\n\n## Overview.*/Ruby InsightVM API Client/' {} +

  # Exclude the setup_workspace directory from the gemspec
  LC_ALL=C perl -0777 -i -pe 's/find \*/find docs lib spec/' rapid7_vm_console.gemspec
fi


if [ "$1" = "go" ]; then
  # Cleanup API documentation strings
  LC_ALL=C find . -type f -exec perl -0777 -i -pe 's/\* InsightVM API(\n\s\*){2} # Overview.*/\* Go InsightVM Client/' {} +
fi

# Cleanup local console details
LC_ALL=C find . -type f -not -path "./.git/*" -exec sed -i '' "s/$2:3780/localhost:3780/g" {} +

git checkout -b release/$CONSOLE_VERSION
git add *
git commit -a -m "Update generated library to version: $LIB_VERSION"
