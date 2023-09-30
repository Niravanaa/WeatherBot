import discord
from discord.ext import commands
import traceback

class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Error handler for command errors
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return  # Ignore unknown commands silently
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing required argument. Please check the command usage.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Invalid argument. Please provide a valid argument.")
        elif isinstance(error, commands.CheckFailure):
            await ctx.send("You do not have permission to use this command.")
        else:
            # Log the error to the console
            print(f"An error occurred: {error}")
            traceback.print_exception(type(error), error, error.__traceback__)

            # Send an error message to the user
            await ctx.send("An error occurred while executing the command. Please try again later.")

def setup(bot):
    bot.add_cog(ErrorHandler(bot))
