import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')
CHANNEL_ID = int(os.getenv('CHANNEL_ID', 0))