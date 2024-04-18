from datetime import datetime, timedelta

def current_time():
    return datetime.now()

def two_weeks_later():
    return current_time() + timedelta(days=14)