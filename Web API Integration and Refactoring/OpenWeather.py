import requests
import json

class OpenWeather:
    def __init__(self, zip=None, ccode=None):
        self.api_key = None
        
        if zip is None:
            zip = "10001"
        self.zip = zip
        
        if ccode is None:
            ccode = "US"
        self.ccode = ccode
        
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        self.weather_data = None
        
    def set_apikey(self, api_key):
        self.api_key = api_key
    
    def load_data(self):
        if self.api_key is None:
            print("Error: API key not set")
            return None
        
        query_params = {"zip": self.zip, "ccode": self.ccode, "appid": self.api_key, "units": "imperial"}
        response = requests.get(self.base_url, params=query_params)
        
        if response.status_code == 200:
            self.weather_data = json.loads(response.content.decode('utf-8'))
        else:
            print(f"Error: Request failed with status code {response.status_code}")
            self.weather_data = None
    
    @property
    def temperature(self):
        if self.weather_data is None:
            print("Error: Weather data not loaded")
            return None
        
        temp = self.weather_data.get("main", {}).get("temp")
        if temp is None:
            print("Error: Temperature data not found")
            return None
        
        return temp
    
    @property
    def high_temperature(self):
        if self.weather_data is None:
            print("Error: Weather data not loaded")
            return None
        
        temp = self.weather_data.get("main", {}).get("temp_max")
        if temp is None:
            print("Error: High temperature data not found")
            return None
        
        return temp
    
    @property
    def low_temperature(self):
        if self.weather_data is None:
            print("Error: Weather data not loaded")
            return None
        
        temp = self.weather_data.get("main", {}).get("temp_min")
        if temp is None:
            print("Error: Low temperature data not found")
            return None
        
        return temp
    
    @property
    def longitude(self):
        if self.weather_data is None:
            print("Error: Weather data not loaded")
            return None
        
        lon = self.weather_data.get("coord", {}).get("lon")
        if lon is None:
            print("Error: Longitude data not found")
            return None
        
        return lon
    
    @property
    def latitude(self):
        if self.weather_data is None:
            print("Error: Weather data not loaded")
            return None
        
        lat = self.weather_data.get("coord", {}).get("lat")
        if lat is None:
            print("Error: Latitude data not found")
            return None
        
        return lat
    
    @property
    def description(self):
        if self.weather_data is None:
            print("Error: Weather data not loaded")
            return None
        
        desc = self.weather_data.get("weather", [{}])[0].get("description")
        if desc is None:
            print("Error: Weather description data not found")
            return None
        
        return desc
    
    @property
    def humidity(self):
        if self.weather_data is None:
            print("Error: Weather data not loaded")
            return None
        
        humidity = self.weather_data.get("main", {}).get("humidity")
        if humidity is None:
            print("Error: Humidity data not found")
            return None
        
        return humidity           

def main():
    zipcode = input("Enter your zip code: ")
    ccode = input("Enter your country code: ")
    apikey = input("Enter your API key: ")

    open_weather = OpenWeather(zipcode, ccode)
    open_weather.set_apikey(apikey)
    open_weather.load_data()

    if open_weather.weather_data is None:
            return

    print(f'The temperature for {zipcode} is {open_weather.temperature} degrees')
    print(f'The high for today in {zipcode} will be {open_weather.high_temperature} degrees')
    print(f'The low for today in {zipcode} will be {open_weather.low_temperature} degrees')
    print(f"The coordinates for {zipcode} are {open_weather.longitude} longitude and {open_weather.latitude} latitude")
    print(f'The current weather for {zipcode} is {open_weather.description}')
    print(f'The current humidity for {zipcode} is {open_weather.humidity}')

if __name__ == "__main__":
    main()
