# WeatherBot
 Neat little RESTful API project that uses Python to obtain relevant weather information.

<img align="right" src="https://i.imgur.com/k4Hk8ro.png" width="50%"/>

<img align="right" src="https://i.imgur.com/4Rqbnz5.png" width="50%"/></p>

## Overview

This is a Discord bot that provides weather information for specified locations. It allows users to check the current weather, weather forecast, and set their weather preferences.

## Features

- Get current weather conditions for a location.
- Fetch weather forecasts, including daily and hourly forecasts.
- Set and manage user-specific weather preferences.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Niravanaa/WeatherBot.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set the TOKEN property in `config.py` to your Discord Bot's token:

```bash
TOKEN="your_bot_token_here"
```

## Usage

- Start the bot:

```bash
python main.py
```

- Use the following Discord commands:
- `!current_weather [location]` - Get current weather conditions.
- `!forecast_weather [location]` - Get weather forecasts.
- `!setprefs [units] [language]` - Set your weather preferences.
- `!getprefs` - Get your current preferences.

## Configuration

- Update `config.py` with your API keys, default settings, and other configurations.
- Customize the bot's behavior by modifying the code in `main.py`.
- Add more features and commands by creating additional cogs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome!

## Acknowledgments

- Thanks to the [Discord.py](https://discordpy.readthedocs.io/en/stable/) library.
- Weather data provided by [WeatherUnlocked.com](https://weatherunlocked.com/).
- Geocoding API provided by [Free Geocoding API](https://geocode.maps.co/).

