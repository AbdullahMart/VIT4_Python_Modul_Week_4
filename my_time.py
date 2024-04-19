from datetime import datetime, timedelta


def current_time():
    return datetime.now().strftime("%Y-%m-%d")

def fourteen_days_later():
    return (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")