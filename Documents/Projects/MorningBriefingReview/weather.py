"""weather data retrieval"""

import requests
import os 
from dotenv import load_dotenv
import logging
import config
logger = logging.getLogger(__name__)





def get_weather():
    """acquire data from api endpoint configured"""
    load_dotenv()

    weathers = os.getenv("WEATHER_KEY")

    api_url = f"{config.WEATHER_API_URL}?key={os.getenv('WEATHER_KEY')}&q={config.WEATHER_LOCATION}"

    try:
        response = requests.get(api_url, timeout=15)
        data = response.json()
        weather = {"temp": data['current']["temp_c"], "humidity": data['current']["humidity"], "uv": data['current']["uv"]}
        return weather
    except Exception as e:
        logger.error(f"Error fetching weather data: {e}")
        fallback = {'temp': "N/A", "humidity": "N/A", "uv": "N/A"}
        return fallback
