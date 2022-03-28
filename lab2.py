import re
import sys

class Student:
  def print(self):
    print("id", self.id)
    print("name", self.name)
    print("DoB", self.DoB)

  def __init__(self, i, n, d):
    self.id = i
    self.name = n
    self.DoB = d
  
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
  
  def get_listStuddent():
    return f'{"id":^20}{"name":^20}{"DoB":^20}
  def get_listStudent(self):
    return f'{self.__id:^20}{self.__name:>20}{self.__DoB:^20}'

class Course:
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

class Validator:
    def __init__(self, user_input, value):
        self.__input = user_input
        self.__pat = re.compile(f'^{value}$')

    def is_ok(self):
        return re.search(self.__pat, self.__input)

    def value(self, value_type=str):
        return value_type(self.__input)

class Container:
    Students = []
    Courses = []
def input_number_of_courses():
    user_input = Validator(input('Enter number of courses: '), '[1-9]+')
    return user_input.value(int) if user_input.is_ok() else -1

def input_number_of_students():
    user_input = Validator(input('Enter number of students: '), '[1-9]+')
    return user_input.value(int) if user_input.is_ok() else -1

def input_student_details():
    user_input_id = Validator(input('Enter student ID: '), '.*')
      user_input_name = Validator(input('Enter student name: '), '[A-Za-z][A-Za-z ]*') 
      user_input_DoB = Validator(input('Enter student date of birth: '), '%D/%M/%Y')
    if user_input_id.is_ok() and user_input_dob.is_ok() and user_input_name.is_ok():
        return tuple(map(Validator.value, [user_input_id, user_input_dob, user_input_name]))
    return (None, None, None)

def input_course_details():
    user_input_id = Validator(input('Enter course ID: '), '.*')
    user_input_name = Validator(input('Enter course name: '), '[A-Za-z][A-Za-z ]*')
    if user_input_id.is_ok() and user_input_name.is_ok():
        return tuple(map(Validator.value, [user_input_id, user_input_name]))
    return (None, None)

if __name__ == '__main__':
  con = Container('Input student detail', input_student_detail),
                ('Input course detail', input_course_detail),
                ('Input course detail', input_detail)
  con.main_loop()
  