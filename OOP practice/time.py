import Date
import Person
from datetime import datetime

class Time:
    def __init__(self, hour, minutes, seconds) -> None:
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds
    def all_to_segs(self) -> int:
        return ((self.hour * 3600) + (self.minutes * 60) + self.seconds)
    def hours_in_decimal(self) -> float:
        seconds = self.all_to_segs()
        return (seconds/3600)
    def minutes_in_decimal(self) -> float:
        seconds = self.all_to_segs()
        return (seconds/60)
    