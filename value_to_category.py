import requests
import urllib3
import json


def assign(ip, user, user_pass, vendor_name):
    base_url = "https://"+ip+":9440/api/nutanix/v3/categories/network_function_provider/"+vendor_name
    s = requests.Session()
    s.auth = (user, user_pass)
    s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
    payload = {"value": vendor_name}
    urllib3.disable_warnings()
    s.put(base_url, data=json.dumps(payload), verify=False).json()