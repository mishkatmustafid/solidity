import json
import os
from solcx import compile_standard, install_solc
from web3 import Web3

with open('./SimpleStorage.sol','r') as file:
  simple_storage_file = file.read()
  
# Compile Our Solidity

install_solc('0.6.0')
compiled_sol = compile_standard(
  {
    "language": "Solidity",
    "sources": {
      "SimpleStorage.sol": {
        "content": simple_storage_file
      }
    },
    "settings": {
      "outputSelection": {
        "*": {
          "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
        }
      }
    }
  },
  solc_version = '0.6.0'
)

with open("compiled_code.json","w") as file:
  json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol['contracts']['SimpleStorage.sol']['SimpleStorage']['evm']['bytecode']['object']

# get abi
abi = compiled_sol['contracts']['SimpleStorage.sol']['SimpleStorage']['abi']

# for connecting to ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
my_address = "0xA26Fd43C4b79f85BD928148172BA1AA4A6c2088D"
private_key = os.getenv("private_key")

# Create the contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
print(SimpleStorage)