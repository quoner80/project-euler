# Counting Sundays
#
# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

#  0 : January
#  1 : February
#  2 : March
#  3 : April
#  4 : May
#  5 : June
#  6 : July
#  7 : August
#  9 : September
#  9 : October
# 10 : November
# 11 : December

# 0 : Sunday
# 1 : Monday
# 2 : Tuesday
# 3 : Wednesday
# 4 : Thursday
# 5 : Friday
# 6 : Saturday

sundays_on_first = 0;

# 1 Jan 1900 was a Monday.
day = 1;

for year in range(1900, 2001):
    for month in range(12):
        # At this point day is the first day of the month. Remember to check only from 1901 onward.
        if year > 1900 and day == 0:
            print "%02d/01/%d was a Sunday." % (month + 1, year);
            sundays_on_first += 1;
        # print "%02d/01/%d was %d." % (month + 1, year, day);
        if month == 8 or month == 3 or month == 5 or month == 10:
            day += 30;
        elif month == 1:
            day += 28;
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                day += 1;
        else:
            day += 31;
        day %= 7;
print "Total Sundays on the first of the month = %d." % sundays_on_first;
