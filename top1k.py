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
mydict = {}
for i in coinIDs:
    #print(i)
    marketData = requests.get(url1 + i + url2)
    #print(marketData.json())
    marketCap = marketData.json()['market_caps'][0][1]
    #print(marketCap)
    volume = marketData.json()['total_volumes'][0][1]
    #print(volume)
    index = coinIDs.index(i)
    if marketCap == 0:
        volumeOverMarketCap = 0
    else:
        volumeOverMarketCap = volume/marketCap
    mydict[index] = [{"Name" : coinNames[index] , "value" : volumeOverMarketCap }]
    print(mydict[index])
    time.sleep(4.1)

# Define the fields/columns for the CSV file
fields = ["Name", "price"]

# Open the CSV file with write permission
with open("topCoinsByVolumeMktCap.csv", "w", newline="") as csvfile:
    # Create a CSV writer using the field/column names
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    
    # Write the header row (column names)
    writer.writeheader()
    
    # Write the data
    for row in mydict:
        writer.writerow(row)
    



    
