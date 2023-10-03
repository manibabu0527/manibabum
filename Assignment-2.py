import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def Fetch_Weather_Data():
    try:
        response = requests.get(API_URL)
        
        response.raise_for_status()
        
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
        return None
def get_temperature(weather_data, date_time):
    for forecast in weather_data['list']:
        if forecast['dt_txt'] == date_time:
            return forecast['main']['temp']
    return None

def get_wind_speed(weather_data, date_time):
    for forecast in weather_data['list']:
        if forecast['dt_txt'] == date_time:
            return forecast['wind']['speed']
    return None

def get_pressure(weather_data, date_time):
    for forecast in weather_data['list']:
        if forecast['dt_txt'] == date_time:
            return forecast['main']['pressure']
    return None

if __name__ == "__main__":
    weather_data = Fetch_Weather_Data()
    
    if not weather_data:
        exit()

    while True:
        print("\nOptions:")
        print("1. Get Temperature")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        option = input("Select an option: ")

        if option == '1':
            date_time = input("Enter date with time (example., '2023-10-02 12:00:00'): ")
            temperature = get_temperature(weather_data, date_time)
            if temperature is not None:
                print(f"Temperature at {date_time}: {temperature}°C")
            else:
                print("Invalid date/time or data not available.")
        elif option == '2':
            date_time = input("Enter date with time (example., '2023-10-02 12:00:00'): ")
            wind_speed = get_wind_speed(weather_data, date_time)
            if wind_speed is not None:
                print(f"Wind Speed at {date_time}: {wind_speed} m/s")
            else:
                print("Invalid date/time or data not available.")
        elif option == '3':
            date_time = input("Enter date with time (example., '2023-10-02 12:00:00'): ")
            pressure = get_pressure(weather_data, date_time)
            if pressure is not None:
                print(f"Pressure at {date_time}: {pressure} hPa")
            else:
                print("Invalid date/time or data not available.")
        elif option == '0':
            break
        else:
            print("Invalid option. Please choose a valid option.")
