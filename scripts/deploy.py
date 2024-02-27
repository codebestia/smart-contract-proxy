from brownie import network,Contract, Storage, StorageV2, TransparentUpgradeableProxy, ProxyAdmin
from scripts.helpers import get_account, encode_function_data, upgrade

def deploy():
    """
    Steps to run
    - Deploy Storage contract
    - Deploy proxy admin
    """
    account = get_account()
    print("Deploying Storage")
    storage =  Storage.deploy({"from":account})
    
    print("Deploying Proxy Admin")
    admin = ProxyAdmin.deploy({"from":account})
    print("Proxy Admin Deployed")
    # initializer = storage.setNumber, 10
    encoded_initializer_function = encode_function_data()

    print("Deploying Proxy")
    proxy = TransparentUpgradeableProxy.deploy(
        storage.address, admin.address, 
        encoded_initializer_function, 
        {"from":account,"gas_limit":1000000}
        )
    print("Proxy deployed  to {proxy.address}. you can upgrade to v2")

    proxy_storage = Contract.from_abi("Storage",proxy.address,storage.abi)
    proxy_storage.setNumber(10,{"from":account}) # storing the value
    print(f"Proxy Call: storage number => {proxy_storage.getNumber()}")

    # Upgrade
    print("Deploying Storage Version 2")
    storageV2 = StorageV2.deploy({"from":account})
    print("StorageV2 deployed")
    print("Upgrading Proxy to StorageV@")
    upgraded_tx = upgrade(
        account,proxy,storageV2.address,admin
    )
    upgraded_tx.wait(1)
    print("Proxy has been upgraded")

    proxy_storage = Contract.from_abi("Storage",proxy.address,storageV2.abi)
    proxy_storage.increment({'from':account}) # running new contract function
    print(proxy_storage.getNumber()) # checking to see it work


def main():
    deploy()