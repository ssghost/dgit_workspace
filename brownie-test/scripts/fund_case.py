from brownie import FundMe
from scripts.deploy import get_account

def recv_c3():
    c3_latest = FundMe[-1]
    account = get_account()
    entry_fee = c3_latest.getEntranceFee()
    c3_latest.recvFund({'from': account, 'value': entry_fee})

def witd_c3():
    c3_latest = FundMe[-1]
    account = get_account()
    c3_latest.witdFund({'from': account})

def main():
    recv_c3()
    witd_c3()