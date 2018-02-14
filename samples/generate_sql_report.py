import rapid7vmconsole
import base64
from time import sleep


def generate_report():
    config = rapid7vmconsole.Configuration(name='Rapid7')
    config.username = 'nxadmin'
    config.password = 'nxpassword'
    config.host = 'https://localhost0:3780'
    config.verify_ssl = False
    config.assert_hostname = False
    config.proxy = None
    config.ssl_ca_cert = None
    config.connection_pool_maxsize = None
    config.cert_file = None
    config.key_file = None
    config.safe_chars_for_path_param = ''

    auth = "%s:%s" % (config.username, config.password)
    auth = base64.b64encode(auth.encode('ascii')).decode()
    client = rapid7vmconsole.ApiClient(configuration=config)
    client.default_headers['Authorization'] = "Basic %s" % auth
    report_client = rapid7vmconsole.ReportApi(client)

    report_id = create_report_sql(report_client, 'Assets', 'select * from dim_asset')
    print(report_id)

    report_instance_id = run_report(report_client, report_id)
    print(report_instance_id)

    report = download_report(report_client, report_id, report_instance_id)
    print(report)

    delete_report(report_client, report_id)


def create_report_sql(client, report_name, sql):
    report_config = rapid7vmconsole.Report(name=report_name, format='sql-query', query=sql, version='2.3.0')
    response = client.create_report(param0=report_config)
    return response.id


def run_report(client, report_id):
    report = client.generate_report(report_id)
    return report.id


def download_report(client, report_id, instance_id):
    report_done = False

    while not report_done:
        report_instance_status = client.get_report_instance(report_id, instance_id).status

        if any(report_instance_status in s for s in ['aborted', 'failed', 'complete']):
            report_done = True

            report_contents = client.download_report(report_id, instance_id)

            return report_contents
        else:
            sleep(30)


def delete_report(client, report_id):
    client.delete_report(report_id)


if __name__ == '__main__':
    generate_report()
