from domains.mark import *
from domains.store import *

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
        return self.__marksheet
    
    
     def export_info(self):
        ds = DataStorage('courses.txt')
        ds.write(f'{self.__id} --- {self.__name} --- {self.__ects}')

     def import_info(self):
        ds = DataStorage('courses.txt')
        self.__id, self.__name, self.__ects = ds.read().split(' --- ')
        self.__ects = int(self.__ects)