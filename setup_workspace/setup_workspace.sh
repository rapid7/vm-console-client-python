#!/bin/bash
# setup_workspace.sh
#
# Purpose: Generation API client for the Rapid7 Nexpose and InsightVM v3 API. Current supported languages: Python, Ruby, Golang
#
# Requirements: Java install and on PATH
#
# Usage:
#  $ ./setup_workspace.sh param1
# * param1: Language for which to generate library (Python, Ruby, Golang)
#
# Output: Generation of api and models based on Rapid7 Nexpose and InsightVM Swagger file

# Download InsightVM/Nexpose Console Version and update package in config.json
VERSION_URL="http://download2.rapid7.com/download/InsightVM/Rapid7Setup-Linux64.bin.version"
CONSOLE_VERSION=$(curl $VERSION_URL)
LIB_VERSION="0.0.1-$CONSOLE_VERSION"
sed -i -E 's/("packageVersion": "0.0.1-)([0-9]+.[0-9]+.[0-9]+)/\1'"$CONSOLE_VERSION"'/g' ./setup_workspace/config.json
echo "Library Version: $LIB_VERSION"

# Environment variable for branch name
echo 'LIB_VERSION='$LIB_VERSION > /var/jenkins_home/propsfile

# Download swagger file
API_FILE_DIR="api-files/"
SWAGGER_FILE=$API_FILE_DIR"console-swagger.json"
SWAGGER_URL="https://help.rapid7.com/insightvm/en-us/api/api.json"
wget $SWAGGER_URL -O $SWAGGER_FILE
# SWAGGER=$(curl $SWAGGER_URL)
# echo "$SWAGGER" > $SWAGGER_FILE

# Manage swagger codegen
CODEGEN_JAR_NAME="swagger-codegen-cli"
CODEGEN_JAR_VERSION="2.3.0"
URL="http://central.maven.org/maven2/io/swagger/$CODEGEN_JAR_NAME/2.3.0/$CODEGEN_JAR_NAME-$CODEGEN_JAR_VERSION.jar"
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
       --git-user-id "rmehilli-r7" \
       --git-repo-id "vm-console-client-python" \
       --release-note "Update generated library to version: $LIB_VERSION" \
       -o ./ -c setup_workspace/config.json
else
  # No changes
  echo 'No changes were made to client'
fi

git add *
git commit -a -m "Update generated library to version: $LIB_VERSION"
