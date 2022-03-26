from scripts.deploy import get_account, deploy_c1

def test_c1():
    account = get_account()
    c1 = deploy_c1()
    c1.updateStorage(42, {'from': account}) 
    assert c1.retrieveStorage() == 42

     