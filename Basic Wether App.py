import requests
import json

API_KEY = "8f98e894c1be1493bb0392d78fe9e756"  # Get from https://openweathermap.org/api


def get_weather_data(location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTP errors
        data = response.json()

        if data["cod"] != 200:
            return None

        return {
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }
    except:
        return None


def main():
    print("=== Weather App ===")
    location = input("Enter city or ZIP code: ").strip()

    weather = get_weather_data(location)
    if not weather:
        print("Error: Invalid location or API issue.")
        return

    print(f"\nCurrent Weather in {location}:")
    print(f"Temperature: {weather['temp']}°C")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Conditions: {weather['description'].capitalize()}")


if __name__ == "__main__":
    main()