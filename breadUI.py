import PySimpleGUI as sg
import random
from discord_webhook import DiscordWebhook

sg.theme('Reddit')   # color (ignore the name)
# please dont touch it really isnt worth it
layout = [  [sg.Text('Webhook:'), sg.InputText(key='poohook')],
            [sg.Button('Send bread'), sg.Button('no 2nd option. just bread.')] ]


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
]

hm = random.choice(bread)

if event == 'Send bread':
	webhook = DiscordWebhook(url=values['poohook'], content=hm)
	response = webhook.execute()


window.close()
