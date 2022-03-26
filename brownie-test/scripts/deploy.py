from brownie import accounts, config, network, SimpleStorage, FundMe, MockV3Aggregator

def deploy_c1():
    account = get_account()
    dContract1 = SimpleStorage.deploy({'from': account})
    print(dContract1.retrieveStorage())
    Txn1 = dContract1.updateStorage(42, {'from':account})
    Txn1.wait(1)
    print(dContract1.retrieveStorage())
    return dContract1

def deploy_c3():
    account = get_account()
    priceFeed = deploy_mock(account)
    dContract3 = FundMe.deploy(priceFeed, {'from': account}, publish_source=config['networks'][network.show_active()].get('verify'))
    print(dContract3.address)
    return dContract3

def get_account():
    if network.show_active() in ['development', 'ganache-local']:
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key']) 

def deploy_mock(account):
    if network.show_active() not in ['development', 'ganache-local']:
        return config['networks'][network.show_active()]['price_feed']
    else:
        if len(MockV3Aggregator) <= 0:
            MockV3Aggregator.deploy(18, 2*10**18, {'from': account})
        return MockV3Aggregator[-1].address

def main():
    deploy_c1()
    deploy_c3()
    