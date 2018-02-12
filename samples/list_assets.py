import rapid7vmconsole
import base64
import logging
import sys

config = rapid7vmconsole.Configuration(name='Rapid7')
config.username = 'nxadmin'
config.password = 'nxpassword'
config.host = 'https://10.3.23.100:3780'
config.verify_ssl = False
config.assert_hostname = False
config.proxy = None
config.ssl_ca_cert = None
config.connection_pool_maxsize = None
config.cert_file = None
config.key_file = None

# Logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
logger.addHandler(ch)
config.debug = False


auth = "%s:%s" % (config.username, config.password)
auth = base64.b64encode(auth.encode('ascii')).decode()
client = rapid7vmconsole.ApiClient(configuration=config)
client.default_headers['Authorization'] = "Basic %s" % auth
asset_api = rapid7vmconsole.AssetApi(client)
assets = asset_api.get_assets()

for a in assets.resources:
    print("Asset ID: %s; Hostname: %s; IP Address: %s" % (a.id, a.host_name, a.ip))
