from brownie import SimpleStorage

def read_c1():
    c1_latest = SimpleStorage[-1]
    print(c1_latest.retrieveStorage())

def main():
    read_c1()
