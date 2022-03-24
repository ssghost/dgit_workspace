from brownie import SimpleStorage

def read_c1():
    c1_latest = SimpleStorage[-1]
    print(c1_latest.retrieveStorage())

if __name__=='__main__':
    read_c1()
