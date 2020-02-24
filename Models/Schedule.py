from Models import Class
from Models import Room
from Models import Subject
from typing import List


class Schedule:
    def __init__(self, num_periods: int, subjects: List[Subject], open_rooms: List[Room]):
        self.subjects = subjects
        self.num_periods = num_periods
        self.matrix = [[[Class(p, s)] for s in subjects] for p in range(num_periods)]
        self.open_rooms = open_rooms
        self.full_rooms = []

    def get_open_class(self, period: int, subject: Subject) -> Class:
        newest_class = self.matrix[period][subject.id][-1]
        if newest_class.is_open():
            return newest_class
        return None

    def create_new_class(self, period: int, subject: Subject) -> Class:
        new_class = Class(period, subject)
        self.matrix[period][subject.id].append(new_class)
        return new_class

    def __str__(self):
        sched = ''
        for p in self.matrix:
            for s in p:
                sched += str(s[0]) + ' | '
            sched += '\n'
        return sched
