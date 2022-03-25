from brownie import accounts, config, network, SimpleStorage, FundMe, MockV3Aggragator

def deploy_c1():
    account = get_account()
    dContract1 = SimpleStorage.deploy({'from': account})
    print(dContract1.retrieveStorage())
    Txn1 = dContract1.updateStorage(42, {'from':account})
    Txn1.wait(1)
    print(dContract1.retrieveStorage())

def deploy_c3():
    account = get_account()
    priceFeed = deploy_mock()
    dContract3 = FundMe.deploy(priceFeed, {'from': account}, publish_source=config['networks'][network.show_active()].get('verify'))
    print(dContract3.address)

def get_account():
    if network.show_active() == 'development':
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key']) 

def deploy_mock():
    if network.show_active() != 'development':
        return config['networks'][network.show_active()]['price_feed']
    else:
        if len(MockV3Aggragator) <= 0:
            MockV3Aggragator.deploy(18, 2*10**18, {'from': account})
        return MockV3Aggragator[-1].address

if __name__=='__main__':
    deploy_c1()
    deploy_c3()