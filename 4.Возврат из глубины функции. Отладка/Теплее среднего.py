def warmer_day(temperature):
    mid = 0
    all = 0

    for week in temperature:
        for t_day in week:
            mid += t_day
            all += 1

    mid_all = (mid / all)

    days = 0

    for week in temperature:
        for day_t in week:
            if day_t > mid_all:
                return days + 1
            else:
                days += 1
