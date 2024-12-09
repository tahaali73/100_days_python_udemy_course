import requests
from datetime import datetime
import time
import smtplib
my_email = "soomrotaha07@gmail.com"
password = "uqvabgefrqbpswkf"
MY_LAT = 33.7215 # Your latitude
MY_LONG = 73.0433 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
print(iss_latitude)
print(MY_LAT)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
   time.sleep(60)
   if ((MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5)) and ((sunset + 3) <= time_now <= (sunrise + 2)):
      
     with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email, to_addrs="tsoomro76@yahoo.com",
                           msg=f"Subject:ISS LOCATION\n\nISS is above you\nlat:{iss_latitude}\nlong:{iss_longitude}\ntime:{time_now}.")
   



