import requests
import os
from twilio.rest import Client

#Open Weather Map // https://openweathermap.org/api/
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = ""

#Twilio // https://console.twilio.com/
account_sid = ""
auth_token = ""

from_phone_number = ""
to_phone_number = ""

#Latlong.net // https://www.latlong.net/
parameters = {
    "lat": 51.499630,
    "lon": -0.035400,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain. Remember to bring an ☂",
        from_=from_phone_number,
        to=to_phone_number
    )
    print(message.status)