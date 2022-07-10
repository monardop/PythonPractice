class Date:
    base_year = 1900
    normal_days = (0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365)
    leap_days = (0, 0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366)
    normal_month = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    leap_month = (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    def __init__(self, day: int, month: int, year: int):
        if self.valid_date(day, month, year) == False:
            print("Invalid date.")
            return
        amountYears = year - self.base_year
        amountDays = amountYears*365 + int(amountYears/4) - int(amountYears/100) + int(amountYears/400)
        self.relative_days = amountDays + self.gregorian_days(day,month,year)
        self.day = day
        self.month = month
        self.year = year
        print(f"Your date is {self.day}/{self.month}/{self.year}. There were {self.relative_days} days from 1900")

    def gregorian_days(self, day: int, month: int, year: int) -> int:
        if self.is_leap(year) == 1:
            return self.normal_days[month] + day
        else: 
            return self.leap_days[month] + day
    def valid_date(self, day: int, month: int, year: int) -> bool:
        if year < self.base_year:
            print("Your year is too old.")
            return False
        if month > 13 or month < 0:
            print("Invalid month entry.")
            return False
        is_leap_year = self.is_leap(year)
        if is_leap_year == 1: 
            if day < 1 and day > self.leap_month[month]:
                print("Invalid days entry.")
                return False
        else:
            if day < 1 and day > self.normal_month[month]:
                print("Invalid days entry.")
                return False
        return True
    def is_leap(self, year: int) -> int:
        return (year % 4 == 0 and (year%100 != 0 or year%400 == 0))