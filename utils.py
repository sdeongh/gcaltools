from datetime import datetime, timedelta


def rfc3339_to_datetime(rfc3339_string):
    return datetime.fromisoformat(rfc3339_string)


def today_date():
    return datetime.now().strftime("%Y-%m-%d")


def next_date():
    return (datetime.now() + timedelta(days=6)).strftime("%Y-%m-%d")
