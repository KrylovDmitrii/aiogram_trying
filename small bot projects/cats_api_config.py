from pprint import pprint
import aiogram
import os

import requests
import time

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')

API_URL = 'https://api.telegram.org/bot'

offset = -2
CATS_URL = 'https://api.thecatapi.com/v1/images/search'

while True:
    updates = requests.get(f'{API_URL}{TOKEN}/getUpdates?offset={offset + 1}').json()
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            if 'text' in result['message']:
                user_text = result['message']['text']
            else:
                user_text = 'Котик'

        response = requests.get(CATS_URL)
        if response.status_code == 200:
            link = response.json()[0]['url']
            requests.get(f'{API_URL}{TOKEN}/sendPhoto?chat_id={chat_id}&photo={link}&caption={user_text}')
        else:
            requests.get(f'{API_URL}{TOKEN}/sendMessage?chat_id={chat_id}&text=Cat not Found')
    user_text = None
