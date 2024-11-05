from web3 import Web3

# 使用 Infura 的 HTTP 连接（以太坊主网）
infura_url = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())
