from datetime import datetime, date, timedelta
# from database import *


class Habit:
    '''the habit class used to create habits consisting of the properties name
    , task to complete, date created and period.'''

    def __init__(self, name: str, task: str, Period: timedelta):
        self.name = name
        self.task = task
        self.date_created = date.today()
        self.Period = Period

    def complete():
        pass


# def check_off(
