import Date
from datetime import datetime
class Person:
    def __init__(self,name: str ,birthday: Date, id: int, sex: str):
        self.id = id
        self.name = name
        self.sex = sex
        self.birthday = birthday
    def get_age(self) -> str:
        today = datetime.now()
        date_today = Date.Date(today.day, today.month, today.year)
        years = date_today.get_years(self.birthday)
        return f"Today {date_today}: {self.name} is {years} old"
