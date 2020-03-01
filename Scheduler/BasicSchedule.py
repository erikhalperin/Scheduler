from Models import Class
from Models import Room
from Models import Schedule
from Models import Student
from Models import Subject
from Models import Teacher

from collections import defaultdict


def main():
    rooms = Room.get_all_rooms()
    all_subjects = [Subject(s) for s in Subject.get_all_subjects()]
    all_students = []
    all_teachers = []
    all_classes = []
    num_periods = 8
    student_subject_conflicts = defaultdict(lambda: [])

    # 3D matrix of num_periods/subjects/classes
    master_schedule = Schedule(num_periods, all_subjects, rooms)

    print(master_schedule)

    for student in all_students:
        for subject in student.subjects:
            while student.has_open_period():
                period = student.get_open_period()

                open_class_optional = master_schedule.get_open_class(period, subject)
                if open_class_optional.is_present():
                    open_class_optional.get().add_student(student)
                else:
                    master_schedule.create_new_class(subject, period).add_student(student)

    

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