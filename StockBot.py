#todo
#function that states if the market is open
#function that gets the average change at market close and open (dow jones?)s
import discord
import datetime as dt
from discord.ext import commands
import os
from dotenv import load_dotenv
from GetStockData import *
import requests

def Configure():
    load_dotenv()


ChanelID = os.getenv('DiscordKey')
#the start of a command prefix. when a user types a $ the bot will be registered
intents = discord.Intents.all()
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix = '$',intents=intents)

@client.event
#sets up first command
async def on_ready():
    print("Bot is loaded")

#Command to see if market is open
#@client.command()
#async def Market():
 #   print(f"The US stock exchange is ")

#COmmand the get the current price and change of stock
@client.command()
async def Price(ctx, ticker: str):
    Curtime = datetime.now()
    Curtime = Curtime.strftime("%H:%M:%S")
    StockData = GetCurrentPrice(ticker)
    match StockData:
        case -1:
             await ctx.send("Invalid Ticker")

        case -2:
            await ctx.send("Failed to locate stock price or change data. Website structure may have changed.")
        case -3:
            await ctx.send(f"Web error {StockData[1]}")
    
        case _:
            await ctx.send(f"{StockData[0]} at {Curtime} with a change of {StockData[1]}")


#command that list all the commands
@client.command()
async def Help(ctx):
    await ctx.send("Price  ticker - Returns the current price and change of a stock at the current time")
    await ctx.send("WIP Market - Returns a if the US stock market is open")
    await ctx.send("Help - Returns all of the commands")
    await ctx.send("About - Returns the project info")

@client.command()
async def About(ctx):
    await ctx.send("Discord Stock Bot")
    await ctx.send("Created by Jacman03")
    await ctx.send("https://github.com/Jackman03")



Configure()
client.run(os.getenv('DiscordKey'))
