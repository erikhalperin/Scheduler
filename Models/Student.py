class Student():
    def __init__(self, name, subjects, total_periods):
        self.name = name
        self.subjects = subjects
        self.open_periods = set(range(1, total_periods+1))

    def has_open_period(self):
        return len(self.open_periods) > 0
