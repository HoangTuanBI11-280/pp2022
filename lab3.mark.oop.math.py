class MarkManager:
    class Mark:
        def __init__(self, value, r_obj=None, e_obj=None):
            self.__value = value
            self.__manager = r_obj
            self.__managee = e_obj

        def get_value(self):
            return self.__value

        def get_object(self, _type):
            if isinstance(self.__manager, _type):
                return self.__manager
            return self.__managee
        

        
        def __init__(self):
          self._marks = []
        
        def inset_mark(self, value, obj=None):
          mark = MarkManager.Mark(value, e_obj=obj)
          self._marks.append(mark)
        
        def get_mark(self, obj=None):
          for mark in self._marks:
            if mark.get_object(obj.__class__) == obj:
              return mark
                return False
        
        def get_average(marks):
          total_sum = sum(marks)
          total_sum = float(total_sum)
          return total_sum / len(marks)
        
        def has_marks(self):
          return bool(self._marks)
class Student(MarkManager):
  def print(self):
    print("id", self.id)
    print("name", self.name)
    print("DoB", self.DoB)

  def __init__(self, student_id, student_dob, student_name):
    self.id = student_id
    self.name = student_name
    self.DoB = student_dob
  
  def __str__(self):
    return f"My id {self.id}. my name {self.name}, my DoB {self.DoB}."
  
  def __init__(self):
    self.__id = 0

  def _get_id(self):
    return self.__id
  
  def get_name(self):
    return self.__name

  def get_DoB(self):
    return self.__DoB
  
  def get_aver(self):
    return self.__aver

  def get_average(marks):
    total_sum = sum(marks)
    total_sum = float(total_sum)
    return total_sum / len(marks)

class Course(MarkManager):
     def print(self):
       print("id", self.id)
       print("name", self.name)
       printf("marksheet", self.marksheet)

      def __init__(self, i, n, d):
        self.id = course_i
        self.name = course_n
        self.marksheet = course_m()
      
      def _get_id(self):
        return self.__id
      
      def get_name(self):
        return self.__name
      
      def get_marksheet(self):
        return self.__marksheet

class Validator:
    def __init__(self, raw_user_input, accept_pattern=None):
        self.__input = raw_user_input
        self.__pat = re.compile(f'^{accept_pattern}$')

    def is_ok(self):
        return re.search(self.__pat, self.__input)

    def value(self, value_type=str):
        return value_type(self.__input)

class Display:
      def accept(self, id, name, DoB, marksheet ):
        ob = Student(id, name, DoB, marksheet )
        ls.append(ob)

      def display(self, ob):
        print("id   : ", ob.id)
        print("name ", ob.name)
        print("DoB : ", ob.DoB)
        print("marksheet : ", ob.marksheet)
        print("\n")

class Search:
  def search(self, rn):
    for i in range(ls.__len__()):
      if(ls[i].rollno == rn):
        return i    

class CommandPrompt:
    state = -1

    def __init__(self, msg, cmd_list=None, pat=None):
        self.__prompt_msg = msg
        self.__cmd_list = cmd_list
        self.__accept_command_pattern = pat
        self.__PS = ['>>>', '->', '--->']
        CommandPrompt.state += 1

    def _list_commands(self):
        self.__cmd_list.list_commands()

    def _execute(self, cmd_num):
        return self.__cmd_list.get_command(cmd_num-1)['callback']()

    def _get_prompt_string(self):
        return self.__PS[CommandPrompt.state]

    def main_loop(self):
        while True:
            self._list_commands()
            cmd = Validator(
                    input(f'{self._get_prompt_string()} {self.__prompt_msg} '),
                    accept_pattern=self.__accept_command_pattern)
            if cmd.is_ok():
                status = self._execute(cmd.value(int))
                if status == -10:
                    CommandPrompt.state -= 1
                    break
                elif status == False:
                    print('Error: Invalid response. Try again.')
            else:
                print('Error: Invalid command. Try again.')

class Container:
    students = []
    courses = []

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

def list_students():
    if len(Container.students) == 0:
        print('No students available.')
    else:
        print('List of students:')
        print(f'{"ID":^15}{"DATE OF BIRTH":^20}{"NAME":^20}{"AVER":^5}')
        for student in Container.students:
            info = f'{student.get_id():^15}'
            info += f'{student.get_dob():^20}'
            info += f'{student.get_name():>20}'
            info += f'{(student.get_aver() if student.get_aver() else "NaN"):>5}'
            print(info)
    print()

def list_courses():
    if len(Container.courses) == 0:
        print('No courses available.')
    else:
        print('List of courses:')
        print(f'{"ID":^15}{"NAME":^50}{"ECTS":^5}{"GRADED":^10}')
        for course in Container.courses:
            info = f'{course.get_id():>15}'
            info += f'{course.get_name():>50}'
            info += f'{course.get_credits():>5}'
            info += f'{course.has_marks():^10}'
            print(info)
    print()

def list_mark_details(course):
    def list_mark_details_specific():
        print(f"Course [{course.get_name()}]'s marksheet:")
        print(f'{"STUDENT NAME":^20}{"MARK":^10}')
        for mark in course.show_marks():
            student = mark.get_object(Student)
            print(f'{student.get_name():<20}{mark.get_value():^10}')
    return list_mark_details_specific

def list_marks():
    cmds = CommandList()
    for course in Container.courses:
        cmds.add(course.get_name(), list_mark_details(course))
    cmds.add('Return to menu', lambda: -10)
    cmdp = CommandPrompt('Choose a course:',
                         cmds,
                         f'[1-{cmds.get_length()}]')
    cmdp.main_loop()

def input_mark_details(course):
    def input_mark_details_specific():
        print(f'Input marks for course [{course.get_name()}]:')
        for student in Container.students:
            user_input_mark = Validator(
                input(f'Enter mark of student [{student.get_name()}]: '),
                '[0-9.]+')
            if user_input_mark.is_ok():
                value = math.floor(user_input_mark.value(float))
                course.add_mark(value, student)
                student.add_mark(value, course)
            else:
                return False
    return input_mark_details_specific

def calculate_aver_student(student):
    def calculate_aver_student_specific():
        print(f'Calculate AVER for student [{student.get_name()}]...')
        student.calculate_aver()
        print(f'Done, AVER = {student.get_aver()}')
    return calculate_aver_student_specific

if __name__ == '__main__':
    curses.wrapper(curse_splash_screen)
    cmdp = CommandPrompt('Enter a command:', CommandList([
                ('Input student info', input_student_info),
                ('Input course info', input_course_info),
                ('Input marks of a course', input_marks),
                ('Show students', list_students),
                ('Show courses', list_courses),
                ('Show marks of a course', list_marks),
                ('Calculate aver of a student', calculate_gpa),
                ('Exit', lambda: -10)]), '[1-8]')
    cmdp.main_loop()

    
  