#!/bin/bash

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
echo "SWAGGER FILE: $SWAGGER_FILE"
SWAGGER_URL="https://help.rapid7.com/insightvm/en-us/api/api.json"
SWAGGER=$(curl $SWAGGER_URL)
echo "$SWAGGER" > $SWAGGER_FILE

# Manage swagger codegen
CODEGEN_JAR_NAME="swagger-codegen-cli"
CODEGEN_JAR_VERSION="2.3.0"
URL="http://central.maven.org/maven2/io/swagger/$CODEGEN_JAR_NAME/2.3.0/$CODEGEN_JAR_NAME-$CODEGEN_JAR_VERSION.jar"
JAR_PATH="setup_workspace/$CODEGEN_JAR_NAME-$CODEGEN_JAR_VERSION.jar"
echo "URL: $URL and PATH: $JAR_PATH"

# Download and write to file
JAR=$(curl $URL)
echo "$JAR" > $JAR_PATH

# Generate Library
CODEGEN_JAR="setup_workspace/$CODEGEN_JAR_NAME-$CODEGEN_JAR_VERSION.jar"
echo "CODEGEN_JAR: $CODEGEN_JAR"

git status --porcelain --untracked-files=no

# Check if changes were made - new console version | new swagger file
if [[ `git status --porcelain --untracked-files=no` ]]; then
  # Changes
  java -jar $CODEGEN_JAR generate -i $SWAGGER_FILE -l $1 \
       --git-user-id \"rmehilli-r7\" \
       --git-repo-id \"vm-console-client-python\" \
       --release-note \"Update generated library to version: $LIB_VERSION\" \
       -o ./ -c setup_workspace/config.json
else
  # No changes
  echo 'No changes were made to client'
fi

git add *
git commit -a -m "Update generated library to version: $LIB_VERSION"
