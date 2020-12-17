from datetime import date, datetime, timedelta, timezone
from dateutil.relativedelta import relativedelta


def timestampt_to_date(date):
    """Converts a timestamp into a human redable date"""
    ts = int(date)
    ts /= 1000
    return datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")


def get_current_date():
    """Returns the current date in Unix timestamp format"""
    return datetime.now().strftime("%s")


def get_relative_delta_date_in_months(number_of_months):
    """Returns a date N months older than initial date"""
    final_date = date.today() + relativedelta(months=-number_of_months)
    return final_date.strftime("%s")