from secrets import API_KEY
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = "{BASE_URL}?appid={API_KEY}&q={city}".format(BASE_URL=BASE_URL, API_KEY=API_KEY, city=city)
response = requests.get(request_url)
data = response.json()

if response.status_code == 200:
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)

    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")

else:
    error = data['message']
    print(error)
