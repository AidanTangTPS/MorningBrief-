"""AI summarisation for email"""
import os
import logging
import config
from openai import OpenAI
from dotenv import load_dotenv
logger = logging.getLogger(__name__)

def get_summary(news):
    """gets summary based on news parameter"""
    load_dotenv()
    
    llmkey = os.getenv("LLM_API_KEY")
     
    client = OpenAI(
        base_url=config.LLM_BASE_URL,
        api_key=llmkey
    )
    try: 
        completion = client.chat.completions.create(
            model=config.LLM_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are writing a short daily news summary for Leo. "
                        "Write like a smart, direct person texting a friend — not a corporate assistant. "
                        "No 'Good morning', no sign-off, no fluff. "
                        "Just bullet points, one line each, plain English. "
                        "State the fact, add context. "
                        "Don't use words like 'significant', 'milestone', 'pivotal', or 'marking a major achievement'. "
                        "Don't editorialize. Just say what happened."
                    )
                },
                {
                    "role": "user", 
                    "content": f"I need a concise briefing on the following report: {news}"
                }
            ],
            temperature=0.5,
            top_p=1,
            max_tokens=1024,
            stream=False
        )

        return completion.choices[0].message.content
    except Exception as e:
        logger.error(f"Endpoint down or error with API KEY {e}")
        return "cant generate news "

