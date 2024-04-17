from datetime import datetime, timedelta

# Here, we are creating our own time program.
# Two dates will be returned: 1. Current time (Date and time of registration) 2. Date when the book should be returned (only date is sufficient)
# Example taken date is 20-09-2023, 10:38 return date is 04-10-2023

def current_time():
    return datetime.now().strftime("%Y-%m-%d")

def fourteen_days_later():
    return (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")