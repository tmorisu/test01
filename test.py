import requests
import urllib3
import json
import input_handler


def main():
    times = input("作成したVMの数を入力してください->")
    uuids = input_handler.create(int(times))
    for vm_uuid in uuids:
        print(vm_uuid)


if __name__ == "__main__":
    main()
