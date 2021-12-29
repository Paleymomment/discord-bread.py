import discord
import random
from discord_webhook import DiscordWebhook, DiscordEmbed


client = discord.Client(self_bot=True)

@client.event
async def on_ready():
    print('ready')
    
    # This can always be changed if you download the python file directly
    if message.content.startswith('spiderman. give me bread.'):
      
