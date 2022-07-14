class Date:
    base_year = 1601
    amount_days = (( 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365),(0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366))
    normal_month = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    leap_month = (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    def __init__(self, day: int, month: int, year: int):
        if self.valid_date(day, month, year) == False:
            return None
            
        amountYears = year - self.base_year
        amountDays = amountYears*365 + int(amountYears/4) - int(amountYears/100) + int(amountYears/400)
        self.relative_days = amountDays + self.gregorian_days(day,month,year)
        self.day = day
        self.month = month
        self.year = year
        print(f"Your date is {self.day}/{self.month}/{self.year}. There were {self.relative_days} days from 1601")

    def gregorian_days(self, day: int, month: int, year: int) -> int:
        return self.amount_days[self.is_leap(year)][month] + day        
    def valid_date(self, day: int, month: int, year: int) -> bool:
        if year < self.base_year:
            print("Your year is too old.")
            return False
        if month > 12 or month < 1:
            print("Invalid month entry.")
            return False
        is_leap_year = self.is_leap(year)
        if is_leap_year == True: 
            if day < 1 or day > self.leap_month[month]:
                print(f"{self.leap_month[month]}")
                print("Invalid days entry.")
                return False
        else:
            if day < 1 or day > self.normal_month[month]:
                print(f"{self.normal_month[month]}")
                print("Invalid days entry.")
                return False
        return True
    def is_leap(self, year: int) -> bool:
        return (year % 4 == 0 and (year%100 != 0 or year%400 == 0))
    def getDMY(self, relDays:int) -> tuple:
        years_passed = int(relDays/365)
        years_completed = int(years_passed * 365 + years_passed / 4 - years_passed / 100 + years_passed / 400)
        while years_completed >= relDays:
            years_passed -= 1
            years_completed = int(years_passed * 365 + years_passed / 4 - years_passed / 100 + years_passed / 400)
        year = self.base_year + years_passed
        years_day = relDays - years_completed
        row = 1 if self.is_leap(year) else 0
        month = 1
        while years_day > self.amount_days[row][month]:
            month += 1
        day = years_day - self.amount_days[row][month - 1]
        print(f"{(day, month, year)}")
        return (day, month, year)
