import requests

url= "https://api.coingecko.com/api/v3/simple/price"
params={"ids":"bitcoin,ethereum,dogecoin","vs_currencies":"usd,vnd"}
response= requests.get(url,params=params)
if response.status_code==200:
    data=response.json()
    btc=data["bitcoin"]["usd"]
    vnd_btc=data["bitcoin"]["vnd"]
    eth=data["ethereum"]["usd"]
    vnd_eth=data["ethereum"]["vnd"]
    doge=data["dogecoin"]["usd"]
    vnd_doge=data["dogecoin"]["vnd"]

    with open("data/price_log.txt","a") as f:
        f.write(f"BTC: {btc:,.2f} USD | VND: {vnd_btc:,.0f} VND\n")
        f.write(f"ETH: {eth:,.2f} USD | VND: {vnd_eth:,.0f} VND\n")
        f.write(f"DOGE: {doge:,.2f} USD | VND: {vnd_doge:,.0f} VND\n")
        f.write("---------------------------\n")




