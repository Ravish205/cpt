#86000secs days and minutes
total_seconds=86000
seconds_in_minute=60
seconds_in_day=86400
seconds_in_hour=3600
total_days=total_seconds//seconds_in_day
total_minutes=total_seconds//seconds_in_minute
total_hours=total_seconds/seconds_in_hour
print(f"for {total_seconds}seconds the no.of days are {total_days}")
print(f"for {total_seconds}seconds the no.of minutes are {total_minutes}")
print(f"for {total_seconds}seconds the no.of minutes are {total_hours}")
#time breakdown
days=total_seconds//seconds_in_day
remaining_seconds=total_seconds%seconds_in_day
hours=remaining_seconds//3600
minutes=(remaining_seconds%3600)//60
seconds=remaining_seconds%60
print(f"\nBreakdown:{days}days,{hours}hours,{minutes}minutes and {seconds}second")