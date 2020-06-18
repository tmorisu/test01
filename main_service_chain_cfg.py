import cluster_uuid
import category
import value_to_category
import network_function
import categories_mapping
import input_handler


def main():
    central_ip = input("CentralのIPアドレスを入力して下さい->")
    central_user_name = input("Centralのusernameを入力して下さい->")
    central_user_pass = input("Centralのpasswordを入力して下さい->")
    vendor_name = input("接続する装置のベンダー名を入力してください->")
    cluster_uuid.get(central_ip, central_user_name, central_user_pass)
    category.create(central_ip, central_user_name, central_user_pass)
    value_to_category.assign(central_ip, central_user_name, central_user_pass, vendor_name)
    print(
        "logging into Prism Central and checking a new category called network_function_provider with " + vendor_name + "created.")
    target_cluster_name = input("NFVMをディプロイ予定のクラスタ名を入力してください->")
    target_cluster_uuid = input("NFVMをディプロイ予定のクラスタUUIDを入力してください->")
    function_chain_name = input("作成するサービスチェインの名前を入力してください->")
    network_function_type = input("network_function_typeを入力してください:INLINEまたはTAP->")
    network_function.create(central_ip, central_user_name, central_user_pass, target_cluster_name, target_cluster_uuid,
                            function_chain_name, vendor_name, network_function_type)
    print("ドキュメントのStep3まで完了しました。")
    # step 4
    times = input("CVMにログインし指定されたコマンドをすべて実行し各NFVMのUUIDをメモした後、作成したNFVMの数を入力してください->")
    uuids = input_handler.create(int(times))
    for vm_uuid in uuids:
        categories_mapping.create(central_ip, central_user_name, central_user_pass, vm_uuid, vendor_name)


if __name__ == "__main__":
    main()
