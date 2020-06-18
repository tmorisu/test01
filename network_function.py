import requests
import urllib3
import json


def create(ip, user, user_pass, name, uuid, fc_name, vendor_name, network_function_type):
    base_url = "https://" + ip + ":9440/api/nutanix/v3/network_function_chains"
    s = requests.Session()
    s.auth = (user, user_pass)
    s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
    payload = {
        "spec": {
            "name": fc_name,
            "resources": {
                "network_function_list": [
                    {
                        "network_function_type": network_function_type,
                        "category_filter": {
                            "type": "CATEGORIES_MATCH_ANY",
                            "params": {"network_function_provider": [vendor_name]}
                        }
                    }
                ]
            },
            "cluster_reference": {
                "kind": "cluster",
                "name": name,
                "uuid": uuid
            }
        },
        "api_version": "3.1.0",
        "metadata": {
            "kind": "network_function_chain"
        }
    }
    urllib3.disable_warnings()
    data = s.post(base_url, data=json.dumps(payload), verify=False).json()
    print(data)
