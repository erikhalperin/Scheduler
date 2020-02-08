class Student:
    def __init__(self, name, subjects, total_periods):
        self.name = name
        self.subjects = subjects
        self.open_periods = set(range(total_periods))

    def add_open_periods(self, periods):
        self.open_periods.union(periods)

    def has_open_period(self):
        return len(self.open_periods) > 0
