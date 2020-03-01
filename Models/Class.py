from Models import Student
from Models import Subject


class Class:
    def __init__(self, period: int, subject: Subject):
        self.name = subject
        self.period = period
        self.subject = subject
        self.room = None
        self.teacher = None
        self.students = []
        self.student_limit = 30

    def add_student(self, student: Student):
        self.students.append(student)

    def is_open(self) -> bool:
        return len(self.students) < self.student_limit

    def __str__(self):
        return 'S={},P={},R={},T={},#={}'.format(self.subject.name, self.period, self.room, self.teacher, len(self.students))
