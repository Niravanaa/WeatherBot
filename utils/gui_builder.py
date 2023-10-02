import discord
import os

class GUIBuilder:
    image_dir = 'static/images/'  # Directory containing weather icons

    def __init__(self, bot):
        self.bot

    # Create a current weather GUI card
    @staticmethod
    def build_current_weather(data, units, language):
        embed = discord.Embed(title="Current Weather", color=0x3498db)

        if language == 'fr':
            temperature_unit = '°C' if units == 'metric' else '°F'
            wind_speed_unit = 'kph' if units == 'metric' else 'mph'
        else:
            temperature_unit = '°F' if units == 'imperial' else '°C'
            wind_speed_unit = 'mph' if units == 'imperial' else 'kph'

        embed.add_field(name="Temperature", value=f"{data['temperature']}{temperature_unit}", inline=True)
        embed.add_field(name="Feels Like", value=f"{data['feels_like_temperature']}{temperature_unit}", inline=True)
        embed.add_field(name="Humidity", value=f"{data['humidity']}", inline=True)
        embed.add_field(name="Wind Speed", value=f"{data['wind_speed']} {wind_speed_unit}", inline=True)
        embed.add_field(name="Wind Direction", value=f"{data['wind_direction_deg']}°", inline=True)
        embed.add_field(name="Conditions", value=data['weather_description'], inline=True)

        icon_path = os.path.join(GUIBuilder.image_dir, data['weather_icon'])
        
        if os.path.exists(icon_path):
            embed.set_thumbnail(url=f"attachment://{data['weather_icon']}")
           
        return embed

    # Create a forecast weather GUI card
    @staticmethod
    def build_forecast_weather(forecast_data, units, language):
        embed = discord.Embed(title="Forecast Weather", color=0x3498db)

        if language == 'fr':
            temperature_unit = '°C' if units == 'metric' else '°F'
            wind_speed_unit = 'kph' if units == 'metric' else 'mph'
        else:
            temperature_unit = '°F' if units == 'imperial' else '°C'
            wind_speed_unit = 'mph' if units == 'imperial' else 'kph'
        
        # Iterate through the forecast data for each day
        # for day_data in forecast_data:
        embed.add_field(
            name="Date",
            value=forecast_data['date'],
            inline=True
        )
        embed.add_field(
            name="Average Temperature",
            value=f"{forecast_data['temperature']}{temperature_unit}",
            inline=True
        )
        embed.add_field(
            name="Feels Like Temperature",
            value=f"{forecast_data['feels_like_temperature']} mm",
            inline=True
        )
        embed.add_field(
            name="Humidity",
            value=f"{forecast_data['humidity']}%",
            inline=True
        )
        embed.add_field(
            name="Wind Speed",
            value=f"{forecast_data['wind_speed']} {wind_speed_unit}",
            inline=True
        )
        embed.add_field(
            name="Wind Direction",
            value=f"{forecast_data['wind_direction_deg']}°",
            inline=True
        )
        embed.add_field(
            name="Weather Description",
            value=forecast_data['weather_description'],
            inline=True
        )
        
        icon_path = os.path.join(GUIBuilder.image_dir, forecast_data['weather_icon'])
    
        if os.path.exists(icon_path):
            embed.set_thumbnail(url=f"attachment://{forecast_data['weather_icon']}")
        
        return embed
        
    