from Models.Class import Class
from Models.Room import Room
from Models.Schedule import Schedule
from Models.Student import Student
from Models.Subject import Subject
from Models.Teacher import Teacher

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
    master_schedule = Schedule(num_periods, all_subjects, len(rooms))

    print(master_schedule)

    for student in all_students:
        for subject in student.subjects:
            period_conflicts = set()
            while student.has_open_period():
                period = student.get_open_period()

                # get open class for subject in period
                open_class = master_schedule.get_open_class(period, subject.id)

                # if no open class, create new class for subject in period with an open room

                # if no open room, add period to period_conflicts

            if len(period_conflicts) > 0:
                student_subject_conflicts[student].append(subject)
                pass

            student.add_open_periods(period_conflicts)


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