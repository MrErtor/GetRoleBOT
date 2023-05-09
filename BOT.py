# GetRoleBOT
# Author Egor localhost - TheErtor

#import libraries
import discord
from discord.ext import commands
from datetime import datetime

# Variabbles
TOKEN = "#"
GUILD_ID = "#"
ROLE_ID = "#"
PREFIX = "!"

# Print time
def print_time():
    now = datetime.now()
    return now.strftime("[%D %H:%M:%S]")

bot = commands.Bot(intents=discord.Intents.all(), command_prefix= PREFIX) # Command Prefix

# ASCII
print(
    " .88888.             dP    888888ba           dP           888888ba   .88888.  d888888P \n"
    "d8'   `88            88    88    `8b          88           88    `8b d8'   `8b    88    \n"
    "88        .d8888b. d8888P a88aaaa8P' .d8888b. 88 .d8888b. a88aaaa8P' 88     88    88    \n"
    "88   YP88 88ooood8   88    88   `8b. 88'  `88 88 88ooood8  88   `8b. 88     88    88    \n"
    "Y8.   .88 88.  ...   88    88     88 88.  .88 88 88.  ...  88    .88 Y8.   .8P    88    \n"
    "` 88888'  `88888P'   dP    dP     dP `88888P' dP `88888P'  88888888P  `8888P'     dP    "
    "\n\n\n"
)

# Start message
print(f"{print_time()} GetRoleBOT Starting...")

# Bot commands
@bot.command()
async def about(ctx):
    await ctx.send('GetRoleBOT - This is an open bot for getting roles on servers in Discord')   
    print_time() # Console time
    print("Output command about to chat") # Console text

# ROLE ("name")
# Get command 
@bot.command()
async def nameGet(ctx): # Command name
    author = ctx.message.author
    guild = bot.get_guild(GUILD_ID) # Discord server ID
    name = guild.get_role(ROLE_ID) # Role ID

    await author.add_roles(name)
    print(f"{print_time()} Give role 'name' ") # Console text

# Remove command
@bot.command()
async def nameRem(ctx): # Command name
    author = ctx.message.author
    guild = bot.get_guild(GUILD_ID) # Discord server ID
    name = guild.get_role(ROLE_ID) # Role ID

    await author.remove_roles(name)
    print(f"{print_time()} Remove role 'name' ") # Console text

# TOKEN
bot.run(TOKEN)
