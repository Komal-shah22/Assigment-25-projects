import requests

def welcome():
    print("\n\t~~~~~~ WELCOME TO THE WEATHER CHECKER ~~~~~~")
    print("This tool fetches real-time weather info for any city you enter.\n")

def get_weather(city, api_key):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            print(f"❌ City '{city}' not found. Please try again.")
            return

        weather = data["weather"][0]["description"].capitalize()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"\n📍 Weather in {city.capitalize()}:")
        print(f"🌤 Condition: {weather}")
        print(f"🌡 Temperature: {temperature}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌬 Wind Speed: {wind_speed} m/s")

    except Exception as e:
        print("❌ Error fetching weather:", e)


API_KEY = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}"

while True:
    welcome()
    city_input = input("Enter a city name to get weather: ").strip()
    get_weather(city_input, API_KEY)

    again = input("\nWould you like to check another city? (yes/no): ").lower().strip()
    if again != "yes":
        print("\n👋 Goodbye! Stay safe and check the weather often!")
        break
