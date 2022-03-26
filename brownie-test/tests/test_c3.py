from scripts.deploy import get_account, deploy_c3

def test_c3():
    account = get_account()
    c3 = deploy_c3()
    entry_fee = c3.getEntranceFee()
    recv_Txn = c3.recvFund({'from': account, 'value': entry_fee})
    recv_Txn.wait(1)
    assert c3.address2amount(account.address) == entry_fee
    witd_Txn = c3.witdFund({'from': account})
    witd_Txn.wait(1)
    assert c3.address2amount(account.address) == 0
    