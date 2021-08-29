import time
import os
import subprocess 
from telegram.ext import Updater

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ip = os.getenv('IP')
subject = os.getenv('SUBJECT_NAME')
token = os.getenv('TOKEN')
chat_id = os.getenv('CHAT_ID')
delay_sec = int(os.getenv('DELAY_SEC', '60'))


updater = Updater(token)
logger = logging.getLogger()

def get_picture_url(state):
    if state:
        return 'https://pischulenok.xyz/are-ya-winning-son/open.png'
    else:
        return 'https://pischulenok.xyz/are-ya-winning-son/close.png'

def describe_state(state):
    if state:
        return f'{subject} came'
    else:
        return f'{subject} left'

def telegram_presence(state):
    text = describe_state(state)
    picture_url = get_picture_url(state)
    updater.bot.sendPhoto(chat_id, picture_url)
    updater.bot.sendMessage(chat_id, text)

def log_presence(state):
    text = describe_state(state)
    logging.info(text)

def ping(host):
    command = ['ping', '-c', '1', host]
    return subprocess.call(command, stdout=subprocess.DEVNULL) == 0

prev_state = None

while True:
    current_state = ping(ip)
    if current_state != prev_state:
        prev_state = current_state
        log_presence(current_state)
        telegram_presence(current_state)
    time.sleep(delay_sec)
    
