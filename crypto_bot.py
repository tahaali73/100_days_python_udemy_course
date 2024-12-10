import requests
import json
import smtplib
my_email = "soomrotaha07@gmail.com"
password = "uqvabgefrqbpswkf"
parameter = {

     "accept": "application/json",
     "x-cg-demo-api-key": "CG-MysHUYZyyEMYJtypaLrturM6",
     "ids" : "solana",
     "vs_currencies" : "usd",
     "include_24hr_change" : "true"

}

response = requests.get("https://api.coingecko.com/api/v3/simple/price",params=parameter)
data = response.json()

solana_price = data['solana']['usd']
solana_24_change = data['solana']['usd_24h_change']


if (10 >= solana_24_change) or (10 <= solana_24_change):
     with smtplib.SMTP("smtp.gmail.com") as connection:
          connection.starttls()
          connection.login(user=my_email,password=password)
          connection.sendmail(from_addr=my_email,to_addrs="tsoomro76@yahoo.com",
                              msg=f"Subject:SOLANA PRICE UPDATE\n\nprice of solana is : {solana_price} usd and it changes {solana_24_change} percent in prevoius 24 hour")
    

print(response.status_code)