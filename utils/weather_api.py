import requests

class WeatherAPI:
    def __init__(self, app_key):
        self.app_key = app_key
        self.base_url = "http://api.weatherunlocked.com"  # Use the correct API URL

    def get_current_weather(self, location, language='en'):
        endpoint = f"/api/current/{location}?lang={language}&{self.app_key}"
        
        print(endpoint)
        
        response = requests.get(self.base_url + endpoint)

        if response.status_code == 200:
            return response.text
        else:
            return None

    def get_forecast_weather(self, location, language='en'):
        endpoint = f"/api/forecast/{location}?lang={language}&{self.app_key}"

        response = requests.get(self.base_url + endpoint)

        if response.status_code == 200:
            return response.text
        else:
            return None
