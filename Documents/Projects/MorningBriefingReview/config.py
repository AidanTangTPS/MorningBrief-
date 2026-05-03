# config.py
import os 

# Weather Configuration
WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"
WEATHER_LOCATION = "Canberra"

# News Configuration
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"
NEWS_SOURCE = "abc-news-au"
NEWS_PAGE_SIZE = 5

# Notion Configuration
NOTION_API_URL = "https://api.notion.com/v1/databases"
NOTION_DB_ID = os.getenv("DATABASE_KEYNOTION") 
NOTION_VERSION = "2022-06-28"

# LLM Configuration
LLM_BASE_URL = "https://integrate.api.nvidia.com/v1"
LLM_MODEL = "meta/llama-3.1-8b-instruct"

#ESPN URL
ESPN_BASE_URL = "https://site.api.espn.com/apis/site/v2/sports/soccer"