from solc import compile_standard
from web3 import Web3
import json
import os
import dotenv

with open("./contracts/SimpleStorage.sol",'r') as f:
    file = f.read()

compiled_file = compile_standard({
    'language': 'Solidity',
    'sources': {"SimpleStorage.sol":{'content':file}},
    'settings': {'outputSelection':{'*': {'*':["abi","metadata","evm.bytecode","evm.bytecode.sourceMap"]}}}
    })

with open("compiled.json",'w') as f:
    json.dump(compiled_file, f)

bytecode = compiled_file["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]
abi = compiled_file["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

myweb3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chain_id = 1337
myaddress = "0xC14605A85b76092B3D0b8B6c1Acc46F1F4029C17"
dotenv.load_dotenv()
pri_key = os.getenv('PRI_KEY')

myContract = myweb3.eth.contract(bytecode=bytecode, abi=abi)
nonce = myweb3.eth.getTransactionCount(myaddress)
transaction = myContract.constructor().buildTransaction(
    {'chainId':chain_id, 'gasPrice': myweb3.eth.gas_price, 'from':myaddress, 'nonce':nonce}
)
signed_Txn = myweb3.eth.account.sign_transaction(transaction, private_key=pri_key)
Txn_hash = myweb3.eth.send_raw_transaction(signed_Txn.rawTransaction)
Txn_receipt = myweb3.eth.wait_for_transaction_receipt(Txn_hash)

depdContract = myweb3.eth.contract(address=Txn_receipt.contractAddress, abi=abi)
print(depdContract.functions.retrieveStorage().call())

store_Txn = depdContract.functions.updateStorage(42).buildTransaction(
    {'chainId':chain_id, 'gasPrice': myweb3.eth.gas_price, 'from':myaddress, 'nonce':nonce+1}
)
signed_store_Txn = myweb3.eth.account.sign_transaction(store_Txn, private_key=pri_key)
st_Txn_hash = myweb3.eth.send_raw_transaction(signed_store_Txn.rawTransaction) 
st_Txn_recpt = myweb3.eth.wait_for_transaction_receipt(st_Txn_hash)
print(depdContract.functions.retrieveStorage().call())


