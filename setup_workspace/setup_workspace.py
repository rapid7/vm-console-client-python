# setup_workspace.py
#
# Purpose: Generation of Python based API client for the Rapid7 Nexpose and InsightVM v3 API
#
# Requirements: Java install and on PATH
#
# Configuration: Update CONSOLE_URL parameter with appropriate value
#
# Output: Generation of api and models based on Rapid7 Nexpose and InsightVM Swagger file
#

import os
import ssl
import urllib.request

# Console connection details to pull swagger file
console_url = "https://localhost:3780"
console_user = "nxadmin"
console_pass = "nxpassword"

# Download swagger codegen jar
codegen_jar_name = "swagger-codegen-cli"
codegen_jar_version = "2.3.0"
url = "http://central.maven.org/maven2/io/swagger/%s/2.3.0/%s-%s.jar" % (codegen_jar_name, codegen_jar_name, codegen_jar_version)

urllib.request.urlretrieve(url, "setup_workspace/%s-%s.jar" % (codegen_jar_name, codegen_jar_version))

# Fetch console version
response = urllib.request.urlopen('http://download2.rapid7.com/download/InsightVM/Rapid7Setup-Linux64.bin.version')
bytes_version = response.read()

# Decode bytes into string and remove newline chars
console_version = bytes_version.decode("utf-8").rstrip()
lib_version = "0.0.1-%s" % console_version

# Manage API release dates
api_file_dir = 'api-files/'

# Download swagger file
swagger_file = api_file_dir + "console-swagger-%s.json" % console_version

with urllib.request.urlopen('https://help.rapid7.com/insightvm/en-us/api/api.json') as u, open(swagger_file, 'wb') as f:
    # Read and decode swagger file
    bytes_swagger = u.read()
    swagger = u.decode("utf-8").rstrip()
    f.write(swagger)

# Generate library
codegen_jar = "setup_workspace/%s-%s.jar" % (codegen_jar_name, codegen_jar_version)
os.system(("java -jar %s generate -i %s -l python "
           "--git-user-id \"rmehilli-r7\" "
           "--git-repo-id \"vm-console-client-python\" "
           "--release-note \"Update generated library to version: %s\" "
           "-o ./ -c setup_workspace/config.json") % (codegen_jar, swagger_file, lib_version))
