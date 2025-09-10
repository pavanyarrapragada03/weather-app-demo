import requests

def get_weather(city):
    API_KEY = "67b10d1a23066723851dfbb282d71d93"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Create full URL
    url = base_url + "appid=" + API_KEY + "&q=" + city + "&units=metric"

    # Send GET request
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather = data['weather'][0]

        print(f"\nWeather Report for {city.capitalize()}:")
        print(f"🌡 Temperature: {main['temp']}°C")
        print(f"💧 Humidity: {main['humidity']}%")
        print(f"🌬 Wind Speed: {wind['speed']} m/s")
        print(f"☁ Condition: {weather['description'].capitalize()}")
    else:
        print("❌ City not found, please check the name!")

# Run the program
city_name = input("Enter city name: ")
get_weather(city_name)
