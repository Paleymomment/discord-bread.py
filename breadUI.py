import PySimpleGUI as sg
import random
import webbrowser
from discord_webhook import DiscordWebhook, DiscordEmbed

sg.theme('DarkGrey3')   # color (ignore the name)
# please dont touch it really isnt worth it
layout = [  [sg.Text('Webhook:'), sg.InputText(key='poohook')],
            [sg.Button('Send bread'), sg.Button('spam bread.')],
            [sg.Button('Github'), sg.Button('Send hot bread pics')],
            [sg.Text('warning: da bread.')],
            [sg.Text('Send bread: It is obvious what it does')],
            [sg.Text('Spam bread: do not press this, just dont')],
            [sg.Text('Send hot bread pics: um...you find out what it does ;)')] ]

# Create the Window
window = sg.Window('BreadHook', layout)
event, values = window.read()


# Main code 

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

hot_bread_pics = [
'https://media.discordapp.net/attachments/770379564329205793/912665983334891520/2u8utqwhrk_hXJpzeLP2PhMaeH2ChyW9B8ZgzHJ3Z2bkN4Ucmt7zM1Edm3bBydvPJSBRCx3-WnZtmrR4OTAm2nQVB4uXAbZYkLLwW_a49vTAGHByyg.png',
'https://media.discordapp.net/attachments/770379564329205793/912665741164171284/Campfire-Bread-Sticks.png?width=569&height=427',
'https://media.discordapp.net/attachments/770379564329205793/912665364528238682/Webp.png?width=847&height=427',
'https://media.discordapp.net/attachments/770379564329205793/912665268524822548/basket-french-bread-near-fire_70216-3225.png?width=537&height=427',
'https://media.discordapp.net/attachments/770379564329205793/912665188078071858/sourdough-large.png?width=638&height=427',
'https://media.discordapp.net/attachments/770379564329205793/912665144885137478/808.png?width=569&height=427',
'https://media.discordapp.net/attachments/770379564329205793/912664970494357534/bloomer-in-oven-cooked.png?width=641&height=427'
]

ew = [
'You like this bread?',
'Wish you could cook me like this',
'oh my fucking god what the fuck is this',
'if only you were as hot as this bread LOL',
'Cook me like this!'
]

url = 'https://github.com/Paleymomment/discord-bread.py'

hm = random.choice(bread)
bruh = random.choice(hot_bread_pics)
eww = random.choice(ew)

if event == 'Send bread':
	webhook = DiscordWebhook(url=values['poohook'], content=hm)
	response = webhook.execute()


if event == 'spam bread.':
	while True:
		webhook = DiscordWebhook(url=values['poohook'], content=hm)
		response = webhook.execute()

if event == 'Github':
	webbrowser.open_new_tab(url)


embed = DiscordEmbed(title=ew, description=hot_bread_pics, color='03b2f8')

if event == 'Send hot bread pics':
	webhook = DiscordWebhook(url=values['poohook'], content=eww)
	response = webhook.execute()

if event == 'Send hot bread pics':
	webhook = DiscordWebhook(url=values['poohook'], content=bruh)
	response = webhook.execute()




window.close()
