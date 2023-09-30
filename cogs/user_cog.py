import discord
from discord.ext import commands
import config

class UserCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Command: !setprefs [units] [language]
    @commands.command(name='setprefs', help='Set your weather preferences')
    async def set_user_preferences(self, ctx, units, language):
        # Validate units and language preferences
        valid_units = ['metric', 'imperial']
        valid_languages = ['en', 'fr']

        if units not in valid_units or language not in valid_languages:
            await ctx.send("Invalid preferences. Please use valid units (metric or imperial) and languages (en, fr).")
            return

        # Store user preferences
        user_id = str(ctx.author.id)
        self.bot.user_preferences[user_id] = {
            'units': units,
            'language': language
        }

        # Confirm preferences set
        await ctx.send(f"Your weather preferences have been set to Units: {units}, Language: {language}")

    # Command: !getprefs
    @commands.command(name='getprefs', help='Get your weather preferences')
    async def get_user_preferences(self, ctx):
        user_id = str(ctx.author.id)
        if user_id in self.bot.user_preferences:
            user_prefs = self.bot.user_preferences[user_id]
            units = user_prefs.get('units', config.DEFAULT_UNITS)
            language = user_prefs.get('language', config.DEFAULT_LANGUAGE)
            await ctx.send(f"Your weather preferences: Units: {units}, Language: {language}")
        else:
            await ctx.send("You have not set any weather preferences yet.")

def setup(bot):
    bot.add_cog(UserCog(bot))
