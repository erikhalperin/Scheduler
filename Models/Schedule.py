from Models.Class import Class


class Schedule:
    def __init__(self, num_periods, subjects, num_open_rooms):
        self.subjects = subjects
        self.num_periods = num_periods
        self.matrix = [[[Class(s, p)] for s in subjects] for p in range(num_periods)]
        self.num_open_rooms = [num_open_rooms-len(subjects) for p in range(num_periods)]

    def get_open_class(self, period, subject_id):
        newest_class = self.matrix[period][subject_id][-1]
        if newest_class.is_open():
            return newest_class

    def __str__(self):
        sched = ''
        for p in self.matrix:
            for s in p:
                sched += str(s[0]) + ' | '
            sched += '\n'
        return sched
