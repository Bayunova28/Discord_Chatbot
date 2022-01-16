# Discord Chatbot (JarvisBOT)
<img src="https://github.com/Bayunova28/Discord_Virtual_Assistant/blob/master/result.png" width="1000">

Discord is growing in popularity. As such, automated processes, such as banning inappropriate users and reacting to user requests are vital for a community to thrive and grow. 
Automated programs that look and act like users and automatically respond to events and commands on Discord are called bot users. Discord bot users (or just bots) have nearly 
unlimited applications. For example, let’s say you’re managing a new Discord guild and a user joins for the very first time. Excited, you may personally reach out to that user 
and welcome them to your community. You might also tell them about your channels or ask them to introduce themselves. The user feels welcomed and enjoys the discussions that 
happen in your guild and they, in turn, invite friends. Over time, your community grows so big that it’s no longer feasible to personally reach out to each new member, but you 
still want to send them something to recognize them as a new member of the guild. With a bot, it’s possible to automatically react to the new member joining your guild. You can 
even customize its behavior based on context and control how it interacts with each new user. JarvisBOT is the name of discord bot for show information the close price of each
ticker stock.

## Install Package
Make sure you have discord, pandas reader, and dotenv  installed. If not install them using pip
```
pip install discord
pip install pandas-reader
pip install -U python-dotenv
```
## Discord API
Before do this project, you must build [discord API](https://discord.com/developers/applications) in order to build chatbot in discord. Here are the steps for build the API :
* New Application (create your chatbot application)
* Bot (add bot on your application)
* OAuth2 (authentication your bot to can response the message)

### Setting up the discord API
```python
client = discord.Client()
load_dotenv()
TOKEN = 'YOUR DISCORD API TOKEN'
```

### Setting up the response of chatbot
```python
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
```

### Setting up connection of chatbot
```python
@client.event
async def on_connect():
    print('JarvisBOT connected to the server!')
```

### Setting up chatbot can join into each channel in discord
```python
@client.event
async def on_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Welcome to the server {member}!')
```
