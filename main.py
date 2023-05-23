from web3 import Web3
from collections import deque
infura_url = 'https://mainnet.infura.io/v3/d6011d3466e84ae19605eb3af98af509'
web3 = Web3(Web3.HTTPProvider(infura_url))

gas_price = web3.eth.gas_price
print(gas_price)