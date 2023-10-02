import discord
from discord.ext import commands
from utils.weather_api import WeatherAPI
from utils.gui_builder import GUIBuilder
import config
import json  # Import the json module
from datetime import datetime

class WeatherCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.weather_api = WeatherAPI(config.WEATHER_API_KEY)

    # Command: !weather [location]
    @commands.command(name='current_weather', help='Get the current weather for a location')
    async def get_current_weather(self, ctx, location):
        # Get user preferences (units and language)
        user_id = str(ctx.author.id)
        units = config.DEFAULT_UNITS
        language = config.DEFAULT_LANGUAGE
        if user_id in self.bot.user_preferences:
            user_prefs = self.bot.user_preferences[user_id]
            units = user_prefs.get('units', config.DEFAULT_UNITS)
            language = user_prefs.get('language', config.DEFAULT_LANGUAGE)

        # Fetch current weather data as JSON
        current_weather_response = self.weather_api.get_current_weather(location, language)

        if current_weather_response:
            # Parse the JSON response
            weather_data = json.loads(current_weather_response)

            # Determine which temperature units to use based on 'units'
            if units == 'metric':
                temp_tag = 'temp_c'
                feels_like_tag = 'feelslike_c'
                wind_speed_tag = 'windspd_kmh'
            elif units == 'imperial':
                temp_tag = 'temp_f'
                feels_like_tag = 'feelslike_f'
                wind_speed_tag = 'windspd_mph'
            else:
                await ctx.send("Invalid units. Please use valid units (metric or imperial).")
                return

            weather_data = {
                "temperature": weather_data[temp_tag],
                "feels_like_temperature": weather_data[feels_like_tag],
                "humidity": weather_data["humid_pct"],
                "wind_speed": weather_data[wind_speed_tag],
                "wind_direction_deg": weather_data["winddir_deg"],
                "weather_description": weather_data["wx_desc"],
                "weather_icon": weather_data["wx_icon"]
            }

            # Build and send a GUI card for current weather
            embed = GUIBuilder.build_current_weather(weather_data, units, language)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Failed to fetch weather data. Please check the location or try again later.")

    # Command: !forecast_weather [location]
    @commands.command(name='forecast_weather', help='Get the current weather for a location')
    async def get_forecast_weather(self, ctx, location):
        # Get user preferences (units and language)
        user_id = str(ctx.author.id)
        units = config.DEFAULT_UNITS
        language = config.DEFAULT_LANGUAGE
        if (user_id) in self.bot.user_preferences:
            user_prefs = self.bot.user_preferences[user_id]
            units = user_prefs.get('units', config.DEFAULT_UNITS)
            language = user_prefs.get('language', config.DEFAULT_LANGUAGE)
        
        # Fetch current weather data as JSON
        forecast_weather_response = self.weather_api.get_forecast_weather(location, language)
        
        if forecast_weather_response:
            # Parse the JSON response
            all_weather_data = json.loads(forecast_weather_response)
            
            # Determine which temperature units to use based on 'units'
            if units == 'metric':
                temp_tag = 'temp_c'
                feels_like_tag = 'feelslike_c'
                wind_speed_tag = 'windspd_kmh'
            elif units == 'imperial':
                temp_tag = 'temp_f'
                feels_like_tag = 'feelslike_f'
                wind_speed_tag = 'windspd_mph'
            else:
                await ctx.send("Invalid units. Please use valid units (metric or imperial).")
                return
            
            days_forecast = all_weather_data.get("Days", [])
                        
            timeframes_1200 = []
            
            for day_forecast in days_forecast:
                timeframes = day_forecast.get("Timeframes", [])
                
                for timestamp in timeframes:
                    
                    if timestamp['utctime'] == 1200:                        
                        parsed_date = datetime.strptime(timestamp['date'], "%d/%m/%Y")
                        
                        # Get the day, month, and year components
                        day = parsed_date.strftime("%d")
                        month = parsed_date.strftime("%B")
                        year = parsed_date.strftime("%Y")
                        
                        # Add suffix to the day (e.g., 1st, 2nd, 3rd, 4th, etc.)
                        if 10 <= int(day) % 100 <= 20:
                            day += "th"
                        else:
                            day_suffix = {1: "st", 2: "nd", 3: "rd"}.get(int(day) % 10, "th")
                            day += day_suffix
                        
                        # Format the date as "day of Month, Year"
                        formatted_date = f"{day} of {month}, {year}"
                    
                        weather_data = {
                            "date": formatted_date,
                            "temperature": timestamp[temp_tag],
                            "feels_like_temperature": timestamp[feels_like_tag],
                            "humidity": timestamp["humid_pct"],
                            "wind_speed": timestamp[wind_speed_tag],
                            "wind_direction_deg": timestamp["winddir_deg"],
                            "weather_description": timestamp["wx_desc"],
                            "weather_icon": timestamp["wx_icon"]
                        }
                        
                        timeframes_1200.append(weather_data)
                        
            # Build and send a GUI card for forecast weather
            for day in timeframes_1200:
                embed = GUIBuilder.build_forecast_weather(day, units, language)
                await ctx.send(embed=embed)
        else:
            await ctx.send("Failed to fetch weather data. Please check the location or try again later.")
                