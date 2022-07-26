from django.http import HttpResponseBadRequest
import Date
import Person
from datetime import datetime

class Time:
    def __init__(self, hour, minutes, seconds) -> None:
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds
    def hours_in_decimal(self) -> float:
        pass
    def all_to_segs(self) -> int:
        return ((self.hour * 3600) + (self.minutes * 60) + self.seconds)
        