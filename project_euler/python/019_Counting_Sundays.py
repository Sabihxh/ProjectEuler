days = 0

month_dict = {
    "jan": 31,
    "feb": 28,
    "mar": 31,
    "apr": 30,
    "may": 31,
    "jun": 30,
    "jul": 31,
    "aug": 31,
    "sep": 30,
    "oct": 31,
    "nov": 30,
    "dec": 31,
}

month_list = [
    "jan",
    "feb",
    "mar",
    "apr",
    "may",
    "jun",
    "jul",
    "aug",
    "sep",
    "oct",
    "nov",
    "dec",
]
days_list = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]


leap_years = len([x for x in range(1, 101) if x % 4 == 0])

# days in 100 years, plus 25 days for leap year,
# minus 1 because 1 jan to 31 dec

total_days = (365 * 100) + 25

sundays = range(1, total_days + 1, 7)


a_dict = {}

c = 1

for year in range(1901, 2001):
    for month in month_list:
        for day in range(1, month_dict[month] + 1):
            if year % 4 == 0 and month == "feb" and day == 28:
                a_dict[c] = day
                c += 1
                a_dict[c] = 29
                c += 1

            else:
                a_dict[c] = day
                c += 1
print a_dict, len(a_dict)

count = 0
for sunday in sundays:
    if a_dict[sunday] == 1:
        print "Sunday on day --- %s" % sunday
        count += 1


print count
