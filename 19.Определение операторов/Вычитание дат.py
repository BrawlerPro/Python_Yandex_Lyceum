class Date:
    def __init__(self, month, day):
        self.month = month
        self.day = day

    def __sub__(self, other):
        date = self.month, self.day
        sumday = 0
        date1 = other.month, other.day
        sumday1 = 0
        totalday = date[1] - date1[1]
        if date[0] == date1[0]:
            return totalday
        else:
            if date[0] == 1:
                sumday = date[1]
            else:
                days = 0
                if date[0] > 1:
                    for i in range(date[0] - 1):
                        i += 1
                        if i <= 7:
                            if i / 2 != i // 2:
                                days += 31
                            else:
                                if i == 2:
                                    days += 28
                                else:
                                    days += 30
                        if i > 7:
                            if i / 2 == i // 2:
                                days += 31
                            else:
                                days += 30
                    days += date[1]
                    sumday = days
            if date1[0] == 1:
                sumday1 = date1[1]
            else:
                days1 = 0
                if date1[0] > 1:
                    for i in range(date1[0] - 1):
                        i += 1
                        if i <= 7:
                            if i / 2 != i // 2:
                                days1 += 31
                            else:
                                if i == 2:
                                    days1 += 28
                                else:
                                    days1 += 30
                        if i > 7:
                            if i / 2 == i // 2:
                                days1 += 31
                            else:
                                days1 += 30
                    days1 += date1[1]
                    sumday1 = days1
            return sumday - sumday1


mar5 = Date(3, 1)
jan1 = Date(1, 1)

print(mar5 - jan1)
print(jan1 - mar5)
print(jan1 - jan1)
print(mar5 - mar5)