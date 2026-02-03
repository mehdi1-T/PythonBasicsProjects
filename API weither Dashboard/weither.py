import requests

api_key = "a63ecff718dc13ce182abe396acd0cf1"  # replace with your OpenWeatherMap API key
city = input("Enter city name: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()  # convert response to Python dictionary

if response.status_code == 200:
    print(f"Weather in {city}: {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']}°C")
else:
    print("City not found or error occurred")
