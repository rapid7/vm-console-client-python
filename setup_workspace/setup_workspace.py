import os
import shutil
import ssl
import urllib.request

# Download swagger codegen jar
jar_name = "swagger-codegen-cli"
jar_version = "2.3.0"
url = "http://central.maven.org/maven2/io/swagger/%s/2.3.0/%s-%s.jar" % (jar_name, jar_name, jar_version)

urllib.request.urlretrieve(url, "%s-%s.jar" % (jar_name, jar_version))

# Download swagger file
console_swagger_path = "https://localhost:3780/api/3/json"
swagger_file = "json"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

with urllib.request.urlopen(console_swagger_path, context=ctx) as u, open(swagger_file, 'wb') as f:
    f.write(u.read())

# Remove previous directories from generation
dirs = ['lib', 'docs', 'spec']

for directory in dirs:
    if os.path.exists(directory):
        shutil.rmtree(directory)

# Generate library
os.system("java -jar %s-%s.jar generate -i %s -l python -o ./ -c config.json" % (jar_name, jar_version, swagger_file))
