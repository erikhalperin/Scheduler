from Models.Class import Class
from Models.Room import Room
from Models.Student import Student
from Models.Subject import Subject
from Models.Teacher import Teacher


def main():
    rooms = Room.all_rooms()
    subjects = Subject.all_subjects()
    students = []
    teachers = []
    classes = []
    periods = 8

    # 3D matrix of periods/subjects/classes

    for student in students:
        for subject in student.subjects:
            conflict_periods = set()
            while student.has_open_period():
                period = student.open_periods.pop()
                # get open class for subject in period
                # if no open class, create new class for subject in period with an open room
                # if no ope


"""
For each student:
    For each subject:
        pick random open_period
        if open class exists for subject in period, add student to class
        else if open room exists in period, create new class in room
        else add student-subject to student_conflicts
"""

main()

"""
8 x Course
1 x Academy
"""