import os
"""Startup Validation"""
def validate_vars():
    required = ["RESEND_API_KEY",
        "NEWS_KEY", 
        "NOTION_KEY",
        "LLM_API_KEY",
        "WEATHER_KEY",
        "GMAIL_ADDRESS"
    ]
    for var in required:
        if var not in os.environ:
            raise EnvironmentError(f"Missing {var}, try to find it or check github secrets")