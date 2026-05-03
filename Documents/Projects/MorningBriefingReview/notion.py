"""Import from notion"""
import requests
import os
import logging
import config
from dotenv import load_dotenv
from datetime import date

logger = logging.getLogger(__name__)


def get_notion():
    """Fetch from notion DB"""
    load_dotenv()

    date_rn = date.today()
    notion = os.getenv("NOTION_KEY")
    url = f"{config.NOTION_API_URL}/{config.NOTION_DB_ID}/query"    
    headers = {
        "Authorization": f"Bearer {notion}",
        "Notion-Version": config.NOTION_VERSION,
        "Content-Type": "application/json"
    }
    
    payload = {
        "filter": {
            "property": "Date",
            "date": {"equals": str(date_rn)}
        }
    }

    try:
        # Added a timeout so the script doesn't hang if Notion is slow
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"API Connection Error: {e}")
        return []

    results = []
    for item in data.get("results", []):
        props = item.get("properties", {})

        # 1. Safe Status Check
        status_data = props.get("Status", {}).get("status")
        status_name = status_data.get("name") if status_data else "No Status"
        
        if status_name == "Done":
            continue

        # 2. Safe Subject Check (Select)
        subject_obj = props.get("Subject", {}).get("select")
        subject_name = subject_obj.get("name") if subject_obj else "General"

        # 3. Safe Name Check (Title)
        title_list = props.get("Name", {}).get("title", [])
        display_name = title_list[0].get("plain_text") if title_list else "Unnamed Task"

        results.append({
            "name": display_name,
            "subject": subject_name,
            "status": status_name
        })
        
    return results
