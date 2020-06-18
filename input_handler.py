def create(times):
    uuids=[]
    for i in range(times):
        uuid = input("VMのUUIDを入力してください->")
        uuids.append(uuid)
    return uuids
