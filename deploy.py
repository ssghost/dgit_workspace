from solc import compile_standard
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
