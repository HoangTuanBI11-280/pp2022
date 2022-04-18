import tarfile
import os
import glob

from domains.container import *

def compress_data():
    with tarfile.open('students.dat', 'w:gz') as tf:
        for filename in ['students.txt', 'courses.txt', 'marks.txt']:
            if os.path.isfile(filename):
                tf.add(filename)

def decompress_data():
    with tarfile.open('students.dat', 'r:gz') as tf:
        tf.extractall()

def import_students_info(data):
    for line in data:
        s = Student()
        s.import_info()
        Container.students.append(s)

def import_courses_info(data):
    for line in data:
        c = Course()
        c.import_info()
        Container.courses.append(c)

def import_marks_info(data):
    for line in data:
        course_name, student_name, value = line.split(' --- ')
        course = next(filter(lambda c: c.get_name() == course_name, Container.courses))
        student = next(filter(lambda s: s.get_name() == student_name, Container.students))
        course.add_mark(float(value), student)
        student.add_mark(float(value), course)

def exit_program():
    compress_data()
    for filename in glob.glob('*.txt'):
        os.remove(filename)
    return -10

from input import *
from output import *

def main():
   curses.wrapper(curse_splash_screen)
   cmdp = CommandPrompt('Enter a command:', CommandList([
                ('Input student info', input_student_info),
                ('Input course info', input_course_info),
                ('Input marks of a course', input_marks),
                ('Show students', list_students),
                ('Show courses', list_courses),
                ('Show marks of a course', list_marks),
                ('Calculate aver of a student', calculate_aver),
               ('Exit', exit_program)]), '[1-8]')
    cmdp.main_loop()
