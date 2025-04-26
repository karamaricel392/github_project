import requests

def fetch_weather_data(city):
    url = f"https://api.weatherapi.com/v1/weather.json?q={city}&apikey=YOUR_API_KEY_HERE"
    response = requests.get(url)
    data = response.json()
    
    return data['current']['temp_c'], data['current']['pressure_mb'], data['current']['humidity_percent']

def main():
    city = input("Enter a city name: ")
    temp, pressure, humidity = fetch_weather_data(city)

    print(f"Temperature in {city}: {temp}°C")
    print(f"Pressure in {city}: {pressure} mb")
    print(f"Humidity in {city}%")

if __name__ == "__main__":
    main()
