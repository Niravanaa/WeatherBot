import requests
import json

class WeatherAPI:
    def __init__(self, app_key):
        self.app_key = app_key
        self.base_url = "http://api.weatherunlocked.com"  # Use the correct API URL

    def get_current_weather(self, location, language='en'):
        geocode_response = requests.get(f"https://geocode.maps.co/search?q={location}")
        
        jsonify_geocode_response = geocode_response.json()
        
        if jsonify_geocode_response:
            new_location = f"{round(float(jsonify_geocode_response[0]['lat']), 2)},{round(float(jsonify_geocode_response[0]['lon']), 2)}"
                        
            endpoint = f"/api/current/{new_location}?lang={language}&{self.app_key}"
        
            response = requests.get(self.base_url + endpoint)
            
            if response.status_code == 200:
                return response.text
            else:
                return None
        else:
            return None
   
    def get_forecast_weather(self, location, language='en'):
        geocode_response = requests.get(f"https://geocode.maps.co/search?q={location}")
        
        jsonify_geocode_response = geocode_response.json()
        
        if jsonify_geocode_response:
            jsonify_geocode_response = geocode_response.json()
            
            new_location = f"{round(float(jsonify_geocode_response[0]['lat']), 2)},{round(float(jsonify_geocode_response[0]['lon']), 2)}"
            
            endpoint = f"/api/forecast/{new_location}?lang={language}&{self.app_key}"
        
            response = requests.get(self.base_url + endpoint)
            
            if response.status_code == 200:
                return response.text
            else:
                return None
        else:
            return None
