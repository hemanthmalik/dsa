def clock_angle(hour, minute):
    minute_fraction = minute/60
    minute_angle = minute_fraction*360
    hour_angle = hour/12*360 + minute_fraction*30
    return abs(hour_angle-minute_angle)

hour, minute = map(int, input('Enter colon(:) separated hour, minute -> ').split(':'))
# hour, minute = 1, 10

print(clock_angle(hour, minute))