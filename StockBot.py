import discord
import datetime as dt
from discord.ext import commands
import os
from dotenv import load_dotenv
from GetStockData import *
import requests

def Configure():
    load_dotenv()

def MarketStatus():
    

ChanelID = os.getenv('DiscordKey')
#the start of a command prefix. when a user types a $ the bot will be registered
intents = discord.Intents.all()
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix = '$',intents=intents)

#Command to see if market is open
@client.command()
async def Market():
    print("The markey ios")
