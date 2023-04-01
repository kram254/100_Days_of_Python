import requests
import json

class OpenWeather:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"
        
    def get_weather(self, city):
        complete_url = self.base_url + "appid=" + self.api_key + "&q=" + city
        response = requests.get(complete_url)
        weather_data = json.loads(response.content.decode('utf-8'))
        return weather_data
    
def main():
    api_key = 'your_api_key_here'
    ow = OpenWeather(api_key)
    city = 'New York'
    weather_data = ow.get_weather(city)
    print(f"Temperature in {city} is {weather_data['main']['temp']} Kelvin")

if __name__ == '__main__':
    main()
