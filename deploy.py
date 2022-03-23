from solc import compile_standard
from web3 import Web3
import json

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
chain_id = 5777
myaddress = "0xC14605A85b76092B3D0b8B6c1Acc46F1F4029C17"
pri_key = "fe041f36a5e19a764788eecc7f071cbea3a89f650e961810a07ea4a4222477f9"

myContract = Web3.eth.contract(bytecode=bytecode, abi=abi)
