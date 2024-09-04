from twikit import Client,TooManyRequests
import time
from datetime import datetime
import csv
from configparser import ConfigParser
from random import randint

MINIMUM_TWEETS = 10
QUERY = 'chatgpt'

import asyncio

USERNAME = 'akhil3794158296'
EMAIL = 'testakhil1306@gmail.com'
PASSWORD = 'akhil1306'

# Initialize client
client = Client('en-US')

async def main():
    await client.login(
        auth_info_1=USERNAME ,
        auth_info_2=EMAIL,
        password=PASSWORD
    )

asyncio.run(main())
