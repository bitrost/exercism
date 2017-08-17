from datetime import datetime
from datetime import timedelta

def add_gigasecond(date):
    gigasecond = 1000000000

    return date + timedelta(seconds=gigasecond)
