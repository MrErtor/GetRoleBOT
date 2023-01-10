# GetRoleBOT
# Author Egor Komarov - TheErtor

#import libraries
import discord
from discord.ext import commands
from datetime import datetime

# Print time
def print_time():
    now = datetime.now()
    asdasdf = now.strftime("[%D %H:%M:%S]")
    print(asdasdf, end=' ')

bot = commands.Bot(intents=discord.Intents.all() , command_prefix= "!") # Command Prefix

# ASCII
print(" .88888.             dP    888888ba           dP           888888ba   .88888.  d888888P ")
print("d8'   `88            88    88    `8b          88           88    `8b d8'   `8b    88    ")
print("88        .d8888b. d8888P a88aaaa8P' .d8888b. 88 .d8888b. a88aaaa8P' 88     88    88    ")
print("88   YP88 88ooood8   88    88   `8b. 88'  `88 88 88ooood8  88   `8b. 88     88    88    ")
print("Y8.   .88 88.  ...   88    88     88 88.  .88 88 88.  ...  88    .88 Y8.   .8P    88    ")
print("` 88888'  `88888P'   dP    dP     dP `88888P' dP `88888P'  88888888P  `8888P'     dP    ")

print("") # SPACE
print("") # SPACE
print("") # SPACE

print_time()
print("GetRoleBOT Starting...")

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
    guild = bot.get_guild('#') # Discord server ID
    name = guild.get_role('#') # Role ID

    await author.add_roles(name)
    print_time() # Console time
    print("Give role 'name' ") # Console text

# Remove command
@bot.command()
async def nameRem(ctx): # Command name
    author = ctx.message.author
    guild = bot.get_guild('#') # Discord server ID
    name = guild.get_role('#') # Role ID

    await author.remove_roles(name)
    print_time() # Console time
    print("Remove role 'name' ") # Console text

# TOKEN
bot.run('#')
