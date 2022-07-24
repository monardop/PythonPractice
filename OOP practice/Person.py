import Date
from datetime import datetime
class Person:
    def __init__(self,name: str ,birthday: Date, id: int):
        self.id = id
        self.name = name
        self.birthday = birthday
        self.age = self.get_age()
    def get_age(self) -> int:
        today = datetime.now()
        date_today = Date.Date(today.day, today.month, today.year)
        years = date_today.get_years(self.birthday)
        if date_today.month <= self.birthday.month: 
            if date_today.day < self.birthday.day:
                years -=1
        return years
    def days_until_bd(self) -> int:
        today = datetime.now()
        today_date = Date.Date(today.day, today.month, today.year)
        if self.birthday.day == 29 and self.birthday.month == 2:
            birthday_date = Date.Date(28, self.birthday.month, today.year)
        else:   
            birthday_date = Date.Date(self.birthday.day, self.birthday.month, today.year)
        days = birthday_date.get_days(today_date)
        if days < 0:
            birthday_date = Date.Date(self.birthday.day, self.birthday.month, today.year + 1)
            days = birthday_date.get_days(today_date)
        if days == 0: 
            print("Happy birthday!")
        return days