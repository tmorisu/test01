import requests
import urllib3
import json


def create(ip, user, user_pass):
    base_url = "https://"+ip+":9440/api/nutanix/v3/categories/network_function_provider"
    s = requests.Session()
    s.auth = (user, user_pass)
    s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
    payload = {"name": "network_function_provider"}
    urllib3.disable_warnings()
    s.put(base_url, data=json.dumps(payload), verify=False).json()
