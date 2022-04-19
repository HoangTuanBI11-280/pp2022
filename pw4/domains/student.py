<<<<<<< HEAD
import math
import numpy as np
from domains.course import *
from domains.mark import *

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

    def __pre_calculate_aver(self):
        self.__credits = []
        self.__mark_values = []
        for mark in self._marks:
            self.__credits.append(mark.get_object(Course).get_credits())
            self.__mark_values.append(mark.get_value())

    def calculate_aver(self):
        self.__pre_calculate_gpa()
        self.__gpa = math.floor(np.average(
=======
import math
import numpy as np
from domains.course import *
from domains.mark import *

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

    def __pre_calculate_aver(self):
        self.__credits = []
        self.__mark_values = []
        for mark in self._marks:
            self.__credits.append(mark.get_object(Course).get_credits())
            self.__mark_values.append(mark.get_value())

    def calculate_aver(self):
        self.__pre_calculate_gpa()
        self.__gpa = math.floor(np.average(
>>>>>>> cc3c9b732e35ebdf1dbfa9bde47c0d946a16af0d
                np.array(self.__mark_values), weights=np.array(self.__credits)))