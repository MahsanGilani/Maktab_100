"""
    class TimeData:
        methods: __init__ , appending_methods, sprftime_method, converting(for converting str into time), subtraction, leap_year, convert to jdatetime
        class attributes: list_of_obj
        
"""

import datetime as dt
import calendar
import jdatetime

"""import your date time format look like this: 2023-09-27 10:53"""


class TimeDate:

    def __init__(self, datetime):
        # use sprftime_method to convert str into datetime object as soon as the object is created
        self.datetime = TimeDate.strptime_method(datetime)

    @staticmethod
    def strptime_method(item):
        date_obj = dt.datetime.strptime(item, "%Y-%m-%d %H:%M:%S")
        return date_obj

    def __sub__(self, other):  # using magic method for subtract
        subtraction = self.datetime - other.datetime
        # total seconds can get the difference in seconds
        return subtraction.total_seconds()

    def counting_leap_year(self, other):
        year1 = self.datetime.year
        year2 = other.datetime.year
        if year1 > year2:
            # az site https://note.nkmk.me/en/python-calendar-leap-year yad greftam ke hamchin methodi vojud dare
            return calendar.leapdays(year2, year1)
        else:
            return calendar.leapdays(year1, year2)

    def converting_to_jdatetime(self):
        obj_year = self.datetime.year
        obj_month = self.datetime.month
        obj_day = self.datetime.day
        jalali_date = jdatetime.date.fromgregorian(
            day=obj_day, month=obj_month, year=obj_year)
        return jalali_date


dt_obj1 = TimeDate("2023-09-27 10:53:25")
dt_obj2 = TimeDate("2010-09-27 09:46:26")
print("Subtraction between two year in second: {}".format(dt_obj1-dt_obj2))
# اون سالی که بزرگتره باید به عنوان پارامتر دوم قرار بگیره وگرنه منفی میشه جواب
print("The number of leap years: {}".format(
    TimeDate.counting_leap_year(dt_obj2, dt_obj1)))

print(dt_obj1.converting_to_jdatetime())
print(dt_obj2.converting_to_jdatetime())

# print("jalali_date for obj 1: {}".format(dt_obj1.converting_to_jdatetime()))
# print("jalali_date for obj 2: {}".format(dt_obj2.converting_to_jdatetime()))
