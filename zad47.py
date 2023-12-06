from datetime import datetime, timedelta

def findMonday(year, week):
    year_start = datetime(year, 1, 1)
    week_start = year_start + timedelta(weeks=week_number - 1)
    monday = week_start + timedelta(days=(0 - week_start.weekday() + 1) % 7)
    return monday

year_number = int(input("podaj rok: "))
week_number = int(input("podaj numer tygodnia: "))
print (findMonday(year_number, week_number))


