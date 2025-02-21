#task 1
import datetime

print()
today = datetime.date.today()
ordinal = today.toordinal()
five_days_ago_ordinal = ordinal - 5
five_days_ago = datetime.date.fromordinal(five_days_ago_ordinal)
print("Five days ago: ", five_days_ago)
print()

#task 2
today2 = datetime.date.today()
ordinal2 = today.toordinal()
yesterday = datetime.date.fromordinal(ordinal2 - 1)
tomorrow = datetime.date.fromordinal(ordinal2 + 1)
print("Yesterday: ", yesterday)
print("Tomorrow: ", tomorrow)
print()

#task 3
time = datetime.datetime.now()
no_microsecond = time.replace(microsecond=0)
print("Time without microsecond: ", no_microsecond)
print()

#task 4
date1 = datetime.datetime(2024, 2, 20, 14, 30, 0)
date2 = datetime.datetime(2024, 2, 21, 16, 45, 0)

seconds_difference = (date2-date1).total_seconds()
print("seconds difference: ", seconds_difference)
print()