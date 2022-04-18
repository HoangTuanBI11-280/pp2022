from domains.student import *
from domains.course import *
from domains.mark import *
from domains.validator import *
from domains.command import *
from domains.container import *

def input_number_of_courses():
    user_input = Validator(input('Enter number of courses: '), '[0-9]+')
    return user_input.value(int) if user_input.is_ok() else -1

def input_number_of_students():
    user_input = Validator(input('Enter number of students: '), '[0-9]+')
    return user_input.value(int) if user_input.is_ok() else -1

def input_student_details():
    user_input_id = Validator(input('Enter student ID: '), '.*')
    user_input_dob = Validator(input('Enter student date of birth: '), '[0-9]{2}/[0-9]{2}/[0-9]{4}')
    user_input_name = Validator(input('Enter student name: '), '[A-Za-z][A-Za-z ]*')
    if user_input_id.is_ok() and user_input_dob.is_ok() and user_input_name.is_ok():
        return tuple(map(Validator.value, [user_input_id, user_input_dob, user_input_name]))
    return (None, None, None)

def input_course_details():
    user_input_id = Validator(input('Enter course ID: '), '.*')
    user_input_name = Validator(input('Enter course name: '), '[A-Za-z][A-Za-z1-9. ]*')
    user_input_ects = Validator(input('Enter course credits: '), '[1-9]')
    if user_input_id.is_ok() and user_input_name.is_ok() and user_input_ects.is_ok():
        return (user_input_id.value(), user_input_name.value(), user_input_ects.value(int))
    return (None, None, None)

def input_student_info():
    n = input_number_of_students()
    if n == -1:
        return False
    for _ in range(n):
        student_id, student_dob, student_name = input_student_details()
        if not (student_id and student_dob and student_name):
            return False
        Container.students.append(Student(student_id, student_dob, student_name))
    return True

def input_course_info():
    n = input_number_of_courses()
    if n == -1:
        return False
    for _ in range(n):
        course_id, course_name, course_ects = input_course_details()
        if not (course_id and course_name and course_ects):
            return False
        Container.courses.append(Course(course_id, course_name, course_ects))
    return True

def input_marks():
    cmds = CommandList()
    for course in Container.courses:
        cmds.add(course.get_name(), input_mark_details(course))
    cmds.add('Return to menu', lambda: -10)
    cmdp = CommandPrompt('Choose a course:',
                         cmds,
                         f'[1-{cmds.get_length()}]')
    cmdp.main_loop()