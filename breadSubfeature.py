import discord
import random
from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = 'enter webhook here'

bread = [
'https://media.discordapp.net/attachments/911951631342530582/912073359590846474/milk-bread.jpg?width=534&height=427',
'https://media.discordapp.net/attachments/911951631342530582/912073359829925969/Pullman-Loaf-Lede-new.jpg?width=759&height=427',
'https://media.discordapp.net/attachments/911951631342530582/912073360085753926/french-bread-small-loaf-side-view-one-dish-kitchen-sq-1200.jpg?width=427&height=427',
'https://media.discordapp.net/attachments/911951631342530582/912073361042071622/White-Bread-Plated-Cravings-11.jpg?width=284&height=427',
'https://media.discordapp.net/attachments/911951631342530582/912073361255964774/Basic-White-Bread.jpg?width=630&height=427',
'https://media.discordapp.net/attachments/911951631342530582/912073361516019802/white-bread_wide-5154ee611e75ed1fa2ce49a16c8ee9b3536759e2.jpg?width=761&height=427',
'https://media.discordapp.net/attachments/765879063067361280/912064534808784896/unknown.jpg',
'https://media.discordapp.net/attachments/770379564329205793/912611948053557288/cobs-product-whole-wheat-loaf-583x400.png',
'https://media.discordapp.net/attachments/770379564329205793/912611916004884490/4MGKCOK2ZVA37H7T7MPJSTWS2Q.png',
'https://media.discordapp.net/attachments/770379564329205793/912611867535495199/IMG_7713-1024x768.png?width=569&height=427',
'https://media.discordapp.net/attachments/770379564329205793/912611783313854464/sk-ultimate-banana-bread.png?width=641&height=427',
'https://media.discordapp.net/attachments/770379564329205793/912611763277660190/Artisan-Bread-square-FS-46.png?width=427&height=427',
'https://media.discordapp.net/attachments/770379564329205793/912611690896580608/QKdG9YYITTyFmA0MOHl3_yeast20bread.png?width=759&height=427',
'https://media.discordapp.net/attachments/770379564329205793/912611653848268820/52524868.png?width=320&height=426',
'https://media.discordapp.net/attachments/770379564329205793/912611628208504942/351269.png',
'https://media.discordapp.net/attachments/770379564329205793/912611381331763220/amish-white-bread-recipe.png?width=427&height=427',
'https://media.discordapp.net/attachments/770379564329205793/912611352604987392/pita.png?width=399&height=427',
'https://media.discordapp.net/attachments/770379564329205793/912611323295182848/Gluten-Free-Bread-Recipe-Card-480x480.png?width=427&height=427',
'https://media.discordapp.net/attachments/770379564329205793/912611296464232458/homemade-bread-500x480.png?width=445&height=427',
'https://media.discordapp.net/attachments/770379564329205793/912611253908807710/351269.png'
]

client = discord.Client(self_bot=True)

@client.event
async def on_ready():
    print('ready')
    
    # This can always be changed if you download the python file directly
    if message.content.startswith('spiderman. give me bread.'):
      webhook = DiscordWebhook(url=webhook, content=bread)
	  response = webhook.execute()
