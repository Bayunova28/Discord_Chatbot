#import library
import discord
import pandas_datareader as web
from dotenv import load_dotenv

#generate discord API
client = discord.Client()
load_dotenv()
TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

#define function to call stock price information of each ticker
def stock_price(ticker):
    df = web.DataReader(ticker, 'yahoo')
    return df['Close'].iloc[-1]

#define function to run response message of chatbot
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$request'):
        await message.channel.send('Hello World! We are currently recording the message!')
    if message.content.startswith('$private'):
        await message.author.send('Hello, I am private sir!')
    if message.content.startswith('$stock_info'):
        if len(message.content.split(' ')) == 2:
            ticker = message.content.split(' ')[1]
            price = stock_price(ticker)
            await message.channel.send(f'Stock price of {ticker} is {price}!')

#define function to call discord chatbot on each channel
@client.event
async def on_connect():
    print('JarvisBOT connected to the server!')

#define function to call discord chatbot to join channel
@client.event
async def on_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Welcome to the server {member}!')

client.run(TOKEN)
