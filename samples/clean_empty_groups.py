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
asset_group_client = rapid7vmconsole.AssetGroupApi(client)
site_client = rapid7vmconsole.SiteApi(client)


def get_all_resources(rvm_client, call, size=500, **kwargs):
    """ Handle pagination and get all resources for a client """
    resources = []
    page = 0
    size = size

    while True:
        try:
            method = getattr(rvm_client, call)
            resp = method(page=page, size=size, **kwargs)
            if resp:
                resources += resp.resources
            page += 1
            if page >= resp.page.total_pages:
                return resources
        except ApiException as e:
            self.logger.error("Exception when calling IVM API: %s\n" % e)


asset_groups = get_all_resources(asset_group_client, 'get_asset_groups', 500)

empty_groups = []
for group in asset_groups:
    print("GroupID: %s \t Asset count: %s" % (group.id, group.assets))
    if group.assets == 0:
        empty_groups.append(group.id)

for group_id in empty_groups:
    asset_group_client.delete_asset_group(int(group_id))


# for a in assets.resources:
#     print("Asset ID: %s; Hostname: %s; IP Address: %s" % (a.id, a.host_name, a.ip))
