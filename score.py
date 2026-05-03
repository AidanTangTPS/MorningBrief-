"""Score API"""
import requests
from datetime import date, timedelta
import logging
from requests.exceptions import RequestException, Timeout
import config
logger = logging.getLogger(__name__)
# https://site.api.espn.com/apis/site/v2/sports/soccer/{league}/scoreboard?dates=YYYYMMDD

def get_data(league, date):
  """fetches from espn api since its free"""
  url = f"{config.ESPN_BASE_URL}/{league}/scoreboard?dates={date}"
  try: 
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
  except Timeout:
    logger.error("Timeout error")
    return []
  except RequestException as e:
    logger.error(f"Error with fetching {league}")
    return []

  if not data.get("events"):
    return []
  results = []
  for event in data['events']:
    results.append({"home":event["competitions"][0]["competitors"][0]["team"]["displayName"], "home_score":event["competitions"][0]["competitors"][0]["score"], "away":event["competitions"][0]["competitors"][1]["team"]["displayName"], "away_score":event["competitions"][0]["competitors"][1]["score"]})

  return results
  
def get_scores():
  yesterday = date.today() - timedelta(days=1)
  formatted_date = yesterday.strftime("%Y%m%d")
  epl = get_data("eng.1", formatted_date)
  laliga = get_data("esp.1", formatted_date)
  return epl + laliga
  