<<<<<<< HEAD
import re

class Validator:
    def __init__(self, raw_user_input, accept_pattern=None):
        self.__input = raw_user_input
        self.__pat = re.compile(f'^{accept_pattern}$')

    def is_ok(self):
        return re.search(self.__pat, self.__input)

    def value(self, value_type=str):
=======
import re

class Validator:
    def __init__(self, raw_user_input, accept_pattern=None):
        self.__input = raw_user_input
        self.__pat = re.compile(f'^{accept_pattern}$')

    def is_ok(self):
        return re.search(self.__pat, self.__input)

    def value(self, value_type=str):
>>>>>>> cc3c9b732e35ebdf1dbfa9bde47c0d946a16af0d
        return value_type(self.__input)