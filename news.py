"""NEWS API"""
import requests
import os 
import logging
from dotenv import load_dotenv
import config
logger = logging.getLogger(__name__)



def get_news():
    """RETRIEVE FROM ENDPOINT"""
    load_dotenv()
    api_url = f"{config.NEWS_API_URL}?sources={config.NEWS_SOURCE}&pageSize={config.NEWS_PAGE_SIZE}&apiKey={os.getenv('NEWS_KEY')}"

    try:
        response = requests.get(api_url, timeout=10)
        data = response.json()
        
        # Grab the 'articles' list and slice the first 5
        top_five = data["articles"][:5]
        
        results = []
        for i in range(len(top_five)):
            results.append(f"{i+1}. {top_five[i]['title']}")
        logger.info("Articles Done.")    
        return results
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching news data: {e}")
        return []
    
   
    
   