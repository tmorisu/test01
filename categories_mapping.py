import requests
import urllib3
import json


def create(ip, user, user_pass, vm_uuid, vendor_name):
    base_url = "https://"+ip+":9440/api/nutanix/v3/vms/"+vm_uuid
    s = requests.Session()
    s.auth = (user, user_pass)
    s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
    payload = {"kind": "cluster"}
    urllib3.disable_warnings()
    data = s.get(base_url, data=json.dumps(payload), verify=False).json()
    data.pop("status")
    nfpd = {"network_function_provider": vendor_name}
    data["metadata"]["categories"] = nfpd
    print(s.put(base_url, data=json.dumps(data), verify=False).json())