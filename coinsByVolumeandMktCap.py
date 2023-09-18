import requests
import json
import time
import csv

#get json list of all coins
response = requests.get(
    "https://api.coingecko.com/api/v3/coins/list?include_platform=false"
)
print(response)
coins = response.json()

#get list of all coin ids
coinIDs = []
coinNames = []
for d in coins:
    id = d["id"]
    coinIDs.append(id)
    name = d["name"]
    coinNames.append(name)
print("number of coins: " + str(len(coinIDs)))

# get marketcap and trading volume by id 
url1 = "https://api.coingecko.com/api/v3/coins/"
url2 = "/market_chart?vs_currency=usd&days=0&interval=daily"
list = []
fieldnames = ["name","24hr volume", "market cap", "volume/mktcap"]
count = 0

with open('coinInfo.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fieldnames)
    # for i in coinIDs[7159:] if api gets throttled at anypoint
    for i in coinIDs:
        marketData = requests.get(url1 + i + url2)
        marketCap = marketData.json()['market_caps'][0][1]
        volume = marketData.json()['total_volumes'][0][1]
        index = coinIDs.index(i)
        if marketCap != 0:
            volumeOverMarketCap = volume/marketCap       
            list.append([i, volume, marketCap, volumeOverMarketCap ])  
            print(list[count])
            print(index)
            writer.writerow(list[count])
            count += 1
            print(count)
        time.sleep(4.5)



    



    
