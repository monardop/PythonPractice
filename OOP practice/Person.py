import Date
from datetime import datetime
class Person:
    def __init__(self,name: str ,birthday: Date, id: int, sex: str):
        self.id = id
        self.name = name
        self.sex = sex
        self.birthday = birthday
    def get_age(self) -> int:
        today = datetime.now()
        date_today = Date.Date(today.day, today.month, today.year)
        print(date_today)
        years = date_today.get_years(self.birthday)
        if date_today.month <= self.birthday.month: 
            if date_today.day < self.birthday.day:
                years -=1
        return years
