from brownie import accounts, config, SimpleStorage

def deploy_c1():
    account = accounts.add(config['wallets']['from_key'])
    dContract1 = SimpleStorage.deploy({'from': account})
    print(dContract1.retrieveStorage())
    Txn1 = dContract1.updateStorage(42, {'from':account})
    Txn1.wait(1)
    print(dContract1.retrieveStorage())
    
if __name__=='__main__':
    deploy_c1()