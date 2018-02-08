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
import shutil
import ssl
import urllib.request

# Console connection details to pull swagger file
console_url = "https://localhost:3780"
console_user = "nxadmin"
console_pass = "nxpassword"

gem_version = "0.0.1"

# Download swagger codegen jar
codegen_jar_name = "swagger-codegen-cli"
codegen_jar_version = "2.3.0"
url = "http://central.maven.org/maven2/io/swagger/%s/2.3.0/%s-%s.jar" % (codegen_jar_name, codegen_jar_name, codegen_jar_version)

urllib.request.urlretrieve(url, "setup_workspace/%s-%s.jar" % (codegen_jar_name, codegen_jar_version))

# Fetch console version
#urllib.request.urlretrieve(console_url + "/api/3/administration/info")

console_version = "6.5.5"

# Manage API release dates
api_file_dir = 'api-files/'
tracking_file = 'api_history.json'
previous_version = '0.0.0'

# Download swagger file
console_swagger_path = console_url + "/api/3/json"
swagger_file = api_file_dir + "console-swagger-%s.json" % console_version

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

with urllib.request.urlopen(console_swagger_path, context=ctx) as u, open(swagger_file, 'wb') as f:
    f.write(u.read())

# Remove previous directories from generation
# dirs = ['lib', 'docs', 'spec']
#
# for directory in dirs:
#     if os.path.exists(directory):
#         shutil.rmtree(directory)

# Generate library
codegen_jar = "setup_workspace/%s-%s.jar" % (codegen_jar_name, codegen_jar_version)
os.system(("java -jar %s generate -i %s -l python "
           "--git-user-id \"rapid7\" "
           "--git-repo-id \"vm-console-client-python\" "
           "--release-note \"Update generated gem to version: %s\" "
           "-o ./ -c setup_workspace/config.json") % (codegen_jar, swagger_file, gem_version))
