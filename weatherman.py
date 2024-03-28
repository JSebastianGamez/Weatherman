import requests

def get_weather(city_name):
    api_key = 1c0636c1a9ff53baae0db739d4b30757  
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = base_url + 'q=' + city_name + '&appid=' + api_key

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        # Extracting data
        main_data = data["main"]
        temperature = main_data["temp"]
        humidity = main_data["humidity"]
        description = data["weather"][0]["description"]

        # Convert temperature from Kelvin to Celsius
        temperature_celsius = temperature - 273.15

        # Display weather information
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature_celsius:.2f}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
    else:
        print("City not found. Please enter a valid city name.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
