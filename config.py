import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
EXCHANGE_RATE_API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')