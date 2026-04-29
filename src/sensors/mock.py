## Random Sensor Input for Logging Testing

import random
from datetime import datetime

def read_light():
    hour_now = datetime.now().hour
    if 6 <= hour_now <= 18:
        return random.randint(300, 800)
    return random.randint(1,50)
def read_moisture():
    return random.randint(20,60)
def read_temperature():
    return random.randint(10, 30)
