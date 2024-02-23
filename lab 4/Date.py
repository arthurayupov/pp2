#1.
from datetime import datetime, timedelta

current_date = datetime.now()
new_date = current_date - timedelta(days=5)

print("Current Date:", current_date)
print("Date after subtracting five days:", new_date)
#2.
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)
#3.
from datetime import datetime

current_datetime = datetime.now()
stripped_datetime = current_datetime.replace(microsecond=0)

print("Original Datetime:", current_datetime)
print("Stripped Datetime:", stripped_datetime)
