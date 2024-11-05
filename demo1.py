from web3 import Web3

# 使用 Infura 的 HTTP 连接（以太坊主网）
infura_url = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())
# 合约的ABI和地址
contract_abi = [...] 
contract_address = '0xContractAddress'

# 获取合约对象
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# 调用合约方法
result = contract.functions.yourFunctionName().call()
print(result)
