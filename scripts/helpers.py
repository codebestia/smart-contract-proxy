from brownie import network, accounts, config
import eth_utils


LOCAL_DEVELOPMENT = ['mainnet-fork','development']


def get_account(env_account = True, index:int=0):
    """
    Get an account
    :params : `env_account` set whether to use the account specified in the env or the one in the brownie accounts list
    True for env, False for config List
    :params: `index` The index of the development account you want to use. defaults to index 0
    """
    if network.show_active() in LOCAL_DEVELOPMENT:
        account = accounts[index]
    else:
        if env_account:
            account = accounts.add(config['wallets']['from'])
        else:
            account = accounts.load("mainaddress")
    return account

def encode_function_data(intializer = None, *args):
    if len(args) <= 0 or not intializer:
        return eth_utils.to_bytes(hexstr = "0x")
    return intializer.encode_input(*args)

def upgrade(account,proxy,new_address,proxy_admin=None,initializer = None,*args):
    transaction = None
    if proxy_admin:
        if initializer:
            encoded_function_call = encode_function_data(initializer,*args)
            transaction = proxy_admin.upgradeAndCall(
                proxy.address,
                new_address,
                encoded_function_call,
                {'from':account}
            )
        else:
            transaction = proxy_admin.upgrade(
                proxy.address,
                new_address,
                {'from':account}
            )
    else:
        if initializer:
            encoded_function_call = encode_function_data(initializer,*args)
            transaction = proxy.upgradeToAndCall(
                new_address,
                encoded_function_call,
                {'from':account}
            )
        else:
            transaction = proxy.upgradeTo(
                new_address,
                {"from":account}
            )
    return transaction


