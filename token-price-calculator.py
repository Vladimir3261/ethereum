import requests

# Api key from https://etherscan.io
etherScanApiKey = 'YOU_API_KEY_HERE'
# Get current ethereum price endpoint on etherscan.io
etherPriceUrl = 'https://api.etherscan.io/api?module=stats&action=ethprice&apikey=' + etherScanApiKey
# Read token price from user input (console)
tokenPrice = float(input('Enter token price in USD: '))
# Make request to etherscan
r = requests.get(etherPriceUrl)
# If etherscan is down - end process.
if r.status_code != 200:
    print("Error on get course data from Etherscan: " + str(r.status_code))
    exit(1)
# Parse json from etherscan
data = r.json()
# Get current price from response JSON
etherPrice = float(data['result']['ethusd'])
# Calculate price for 1 token in ether
etherPerToken = tokenPrice / etherPrice
# Calculate price for 1 token in wei (for smart-contract)
weiPerToken = int(etherPerToken * 1E18)
# Print all calculations
print("------------------------------------------------")
print("Token price: " + str(tokenPrice) + " USD")
print("Ether price: " + str(etherPrice) + " USD")
print("Count ether for 1 token: " + str(etherPerToken))
print("WEI for 1 token: " + str(weiPerToken))
