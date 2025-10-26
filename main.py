import requests
from twilio.rest import Client

endpoint =  "https://api.openweathermap.org/data/2.5/forecast"

api = "usey23our23api23kasdlkja;"
account_sid = "usey23ou23radfaj232dfldjlfk"
auth_token = "asdjflkjalsf23lkajsdlf2323jasldjkflkasjd"

weather_params = {"lat":21.1702,
                    "lon": 72.8311,
                  "appid": api,
                  "cnt": 4

}

forcast = requests.get(endpoint, params=weather_params)
forcast.raise_for_status()
weather_data = forcast.json()


will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Lele lele umbrella lele",
        from_="+11234567890",
        to="+910987654321",
    )

    print(message.status)