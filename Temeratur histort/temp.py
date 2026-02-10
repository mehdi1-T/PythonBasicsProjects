daily_temps = (18, 21, 19, 23, 22, 20, 17)

hotest_day = max(daily_temps)
coldest_day = min(daily_temps)
average_temp = sum(daily_temps) / len(daily_temps)

print(f"hotest day {hotest_day}")
print(f"coldest day {coldest_day}")
print(f"average temp {average_temp}")