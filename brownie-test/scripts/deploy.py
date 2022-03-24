from brownie import accounts, config, network, SimpleStorage

def deploy_c1():
    account = get_account()
    dContract1 = SimpleStorage.deploy({'from': account})
    print(dContract1.retrieveStorage())
    Txn1 = dContract1.updateStorage(42, {'from':account})
    Txn1.wait(1)
    print(dContract1.retrieveStorage())

def get_account():
    if network.show_active() == 'development':
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key']) 

if __name__=='__main__':
    deploy_c1()