import requests
import urllib3
import json


def get(ip, user, user_pass):
    base_url = "https://"+ip+":9440/api/nutanix/v3/clusters/list"
    s = requests.Session()
    s.auth = (user, user_pass)
    s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
    payload = {"kind": "cluster"}
    urllib3.disable_warnings()
    data = s.post(base_url, data=json.dumps(payload), verify=False).json()
    print("このcentralで管理されているクラスターを表示します")
    for e in data["entities"]:
        print("クラスタ名:"+e["status"]["name"]+", uuid:"+e['metadata']['uuid'])
