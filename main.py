import discord
from discord.ext import commands
import config
import logging
from cogs import weather_cog, user_cog
from logging.handlers import RotatingFileHandler

# Define the intents your bot will use
intents = discord.Intents.default()
intents.message_content = True

# Create an instance of the bot with the intents and a forward slash prefix
bot = commands.Bot(command_prefix=config.WEATHER_COMMAND_PREFIX, intents=intents)

# Initialize user_preferences as an empty dictionary
bot.user_preferences = {}

# Load cogs (extensions)
initial_extensions = [
    weather_cog.WeatherCog(bot),
    user_cog.UserCog(bot)
]

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    await bot.change_presence(activity=discord.Game(name=f"{config.WEATHER_COMMAND_PREFIX}help"))
    for extension in initial_extensions:
        try:
            await bot.add_cog(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}: {e}')

# Configure the logger
logger = logging.getLogger('discord_bot')
logger.setLevel(logging.DEBUG)

# Create a log formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a rotating file handler for bot activity logs
activity_handler = RotatingFileHandler('logs/bot_activity.log', maxBytes=1000000, backupCount=5)
activity_handler.setLevel(logging.INFO)
activity_handler.setFormatter(formatter)

# Create a rotating file handler for error logs
error_handler = RotatingFileHandler('logs/error.log', maxBytes=1000000, backupCount=5)
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(activity_handler)
logger.addHandler(error_handler)

# Run the bot with your token
bot.run(config.BOT_TOKEN)
