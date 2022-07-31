import Date
import Person
from datetime import datetime

class Time:
    def __init__(self) -> None:
        self.hour, self.minutes, self.seconds = self.valid_entry()
        self.relTime = self.int_seconds()
    
    def valid_entry(self) -> tuple:
        entry = input("Insert time in format <<hh:mm:ss>>: ")
        time_new = entry.split(":")
        hour, minutes, seconds = time_new
        if int(minutes) > 59 or int(minutes) < 0 or int(seconds) > 59 or int(seconds) < 0:
            print("Invalid entry")
        return (int(hour), int(minutes), int(seconds))
    def int_seconds(self) -> int:
        return ((self.hour * 3600) + (self.minutes * 60) + self.seconds)
    def float_hours(self) -> float:
        seconds = self.int_seconds()
        return (seconds/3600)
    def float_minutes(self) -> float:
        seconds = self.int_seconds()
        return (seconds/60)
    def show_AMPM(self) -> str:
        if self.hour < 12:
            return f"{self.hour}:{self.minutes}:{self.seconds} AM"
        else:
            return f"{self.hour - 12}:{self.minutes}:{self.seconds} PM"
    def __add__(self, time2):
        new_time = self.int_seconds() + time2.int_seconds()
        self.format_time(new_time)
    def __sub__(self, time2):
        seconds = self.int_seconds() - time2.int_seconds()
        if seconds < 0:
            print("Wrong entry")
        self.format_time(seconds)
    def __str__(self) -> str:
        return f"{self.hour}:{self.minutes}:{self.seconds}"
    def format_time(self, seconds: int):
        hour = int(seconds/3600)
        seconds -= hour
        minutes = int(seconds/60)
        seconds -= minutes
        return Time(hour, minutes, seconds)
    