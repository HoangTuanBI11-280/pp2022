<<<<<<< HEAD
from input import *
from output import *

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
=======
from input import *
from output import *

   curses.wrapper(curse_splash_screen)
   cmdp = CommandPrompt('Enter a command:', CommandList([
                ('Input student info', input_student_info),
                ('Input course info', input_course_info),
                ('Input marks of a course', input_marks),
                ('Show students', list_students),
                ('Show courses', list_courses),
                ('Show marks of a course', list_marks),
                ('Calculate aver of a student', calculate_aver),
    cmdp.main_loop()
>>>>>>> cc3c9b732e35ebdf1dbfa9bde47c0d946a16af0d
