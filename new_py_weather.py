import requests

def weather_forecast(api_key, city):
    # URL for getting weather forecast
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
    
    try:
        # response = requests.get(url)
        forecast = requests.get(url)

        # Check if the response was successful
        forecast.raise_for_status()

        # Get the JSON data from the response
        data = forecast.json()
        print("")
        print(f"Weather forecast for {city}:")
        print("*************************************************")

        hours = data["list"][:8]  # get forecast for next 24 hours
        for time in hours:
            # Create a function to get the weather description
            get_weather_description(time)

    # except requests.exceptions.HTTPError as e:
    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching weather data:", e)

# Create a function to get the weather description
def get_weather_description(time):
    timestamp = time["dt_txt"]
    weather_description = time["weather"][0]["description"]
    temperature = time["main"]["temp"]
    min_temp = time["main"]["temp_min"]
    max_temp = time["main"]["temp_max"]
    humidity = time["main"]["humidity"]
    wind = time["wind"]
    wind_speed = wind["speed"]
    wind_direction = wind["deg"]
    pressure = time["main"]["pressure"]
    sea_level = time["main"]["sea_level"]
    ground_level = time["main"]["grnd_level"]
    gust = wind["gust"]
    visibility = time["visibility"]
    temp_kf = time["main"]["temp_kf"]
    clouds = time["clouds"]
    all = clouds["all"]
    
    # Print the weather forecast
    print("*************************************************")
    print("Timestamp for forecast:", timestamp)
    print("Weather Description:", weather_description)
    print("Temperature:", temperature, "K")
    print("Minimum Temperature:", min_temp, "K")
    print("Maximum Temperature:", max_temp, "K")
    print("Percentage of Humidity:", humidity, "%")
    print("Speed of Wind:", wind_speed, "m/s")
    print("Direction of Wind:", wind_direction, "degrees")
    print("Pressure:", pressure, "hPa")
    print("Sea level:", sea_level)
    print("Ground level:", ground_level)
    print("Gust:", gust)
    print("Visibility:", visibility)
    print("Temp kf:", temp_kf)
    print("Clouds:", all, "%")
    print("")


if __name__ == "__main__":
    # api_key obtained from openweathermap.org
    api_key = "04382c32a382592453e3cff3fdf5fc45"
    # city = "London"
    city = input("Enter a city name: ")
    # Call get_weather_forecast() function by passing api_key and city
    weather_forecast(api_key, city)
