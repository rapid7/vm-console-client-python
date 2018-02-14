# ScanTemplateAssetDiscovery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collect_whois_information** | **bool** | Whether to query Whois during discovery. Defaults to &#x60;false&#x60;. | [optional] 
**fingerprint_minimum_certainty** | **float** | The minimum certainty required for a fingerprint to be considered valid during a scan. Defaults to &#x60;0.16&#x60;. | [optional] 
**fingerprint_retries** | **int** | The number of fingerprinting attempts made to determine the operating system fingerprint. Defaults to &#x60;4&#x60;. | [optional] 
**ip_fingerprinting_enabled** | **bool** | Whether to fingerprint TCP/IP stacks for hardware, operating system and software information. | [optional] 
**send_arp_pings** | **bool** | Whether ARP pings are sent during asset discovery. Defaults to &#x60;true&#x60;. | [optional] 
**send_icmp_pings** | **bool** | Whether ICMP pings are sent during asset discovery. Defaults to &#x60;false&#x60;. | [optional] 
**tcp_ports** | **list[int]** | TCP ports to send packets and perform discovery. Defaults to no ports. | [optional] 
**treat_tcp_reset_as_asset** | **bool** | Whether TCP reset responses are treated as live assets. Defaults to &#x60;true&#x60;. | [optional] 
**udp_ports** | **list[int]** | UDP ports to send packets and perform discovery. Defaults to no ports. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


