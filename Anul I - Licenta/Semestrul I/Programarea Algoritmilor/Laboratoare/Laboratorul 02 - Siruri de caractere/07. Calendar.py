days = ("duminica", "luni", "marti", "miercuri", "joi", "vineri", "sambata")

months = { # 'month': (monthCalendarIndex, monthDays <for common year>)
    'ianuarie': (1, 31),'februarie': (2, 28), 'martie': (3, 31),'aprilie': (4, 30),'mai': (5, 31),
    'iunie': (6, 30), 'iulie': (7, 31), 'august': (8, 31), 'septembrie': (9, 30), 'octombrie': (10, 31),
    'noiembrie': (11, 30), 'decembrie': (12, 31)
} 

def leapYear(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def computeDay(sourceDay, sourceMonth, sourceYear):
    refDate = (1, 1, 1702)
    totalDays = 0
    for year in range (refDate[2], sourceYear):
        totalDays += 366 if leapYear(year) else 365

    for month in months:
        if months[month][0] == sourceMonth:
            break
        if (month == 'februarie' and leapYear(sourceYear)):
            totalDays += 1
        totalDays += months[month][1]

    totalDays += sourceDay - 1
    print("Zile de la 01.01.1702: {}".format(totalDays))
    return days[totalDays % 7].capitalize()

def getInput():
    try:
        day, month, year = input().strip().split()
        day = int(day)
        if (day < 1 or day > 31):
            print("Zi incorecta!")
            exit()
        year = int(year)
        try:
            month = months[month.lower()][0]
            if (month < 1 or month > 12):
                print("Luna incorecta!")
                exit()
        except:
            month = int(month)
        return day, month, year
    except:
        print("Numar incorect de valori / Format gresit!")
        exit()

day, month, year = getInput()
calendarDay = computeDay(day, month, year)
print("Ziua din aceasta data este: {}".format(calendarDay))