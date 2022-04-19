<<<<<<< HEAD
from domains.mark import *

class Course(MarkManager):
     def print(self):
       print("id", self.id)
       print("name", self.name)
       print("marksheet", self.marksheet)
       


     def __init__(self, course_i, course_n, course_m):
        self.id = course_i
        self.name = course_n
        self.marksheet = course_m()
      
     def _get_id(self):
        return self.__id
      
     def get_name(self):
        return self.__name
      
     def get_marksheet(self):
=======
from domains.mark import *

class Course(MarkManager):
     def print(self):
       print("id", self.id)
       print("name", self.name)
       print("marksheet", self.marksheet)
       


     def __init__(self, course_i, course_n, course_m):
        self.id = course_i
        self.name = course_n
        self.marksheet = course_m()
      
     def _get_id(self):
        return self.__id
      
     def get_name(self):
        return self.__name
      
     def get_marksheet(self):
>>>>>>> cc3c9b732e35ebdf1dbfa9bde47c0d946a16af0d
        return self.__marksheet