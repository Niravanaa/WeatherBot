# WeatherBot
 Neat little (soon-to-be) RESTful API project that uses Python to obtain relevant weather information.

## Overview

This is a Discord bot that provides weather information for specified locations. It allows users to check the current weather, weather forecast, and set their weather preferences.

## Features

- Get current weather conditions for a location.
- Fetch weather forecasts, including daily and hourly forecasts.
- Set and manage user-specific weather preferences.
- ...

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/discord-weather-bot.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your Discord bot token:

```bash
DISCORD_TOKEN=your_bot_token_here
```

## Usage

- Start the bot:

```bash
python main.py
```

- Use the following Discord commands:
- `!weather [location]` - Get current weather conditions.
- `!forecast [location]` - Get weather forecasts.
- `!setprefs [units] [language]` - Set your weather preferences.
- `!getprefs` - Get your current preferences.
- ...

## Configuration

- Update `config.py` with your API keys, default settings, and other configurations.
- Customize the bot's behavior by modifying the code in `main.py`.
- Add more features and commands by creating additional cogs.

## Tests

- Run unit tests:

```bash
python -m unittest discover tests
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome!

## Acknowledgments

- Thanks to the [Discord.py](https://discordpy.readthedocs.io/en/stable/) library.
- Weather data provided by [WeatherUnlocked.com](https://weatherunlocked.com/).

