from brownie import accounts, SimpleStorage

def test_deploy():
    account = accounts[0]
    c1 = SimpleStorage.deploy({'from': account})
    assert c1.retrieveStorage() == 0

def test_update():
    account = accounts[0]
    c1 = SimpleStorage.deploy({'from': account})
    c1.updateStorage(42, {'from': account}) 
    assert c1.retrieveStorage() == 42

     