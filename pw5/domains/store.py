<<<<<<< HEAD
class DataStorage:
    __reading = False
    __read_linecount = 0
    __read_data = None

    def __init__(self, file_name):
        self.__file = file_name

    def write(self, data):
        with open(self.__file, 'a') as f:
            f.write(data)
            f.write('\n')

    def __read_next_line(self):
        DataStorage.__read_linecount += 1
        return DataStorage.__read_data[DataStorage.__read_linecount - 1]

    def read(self):
        if not DataStorage.__reading:
            DataStorage.__reading = True
            with open(self.__file, 'r') as f:
                DataStorage.__read_data = f.read().splitlines()
        elif DataStorage.__read_linecount == len(DataStorage.__read_data):
            DataStorage.__reading = False
            DataStorage.__read_linecount = 0
            DataStorage.__read_data = None
            return self.read()
=======
class DataStorage:
    __reading = False
    __read_linecount = 0
    __read_data = None

    def __init__(self, file_name):
        self.__file = file_name

    def write(self, data):
        with open(self.__file, 'a') as f:
            f.write(data)
            f.write('\n')

    def __read_next_line(self):
        DataStorage.__read_linecount += 1
        return DataStorage.__read_data[DataStorage.__read_linecount - 1]

    def read(self):
        if not DataStorage.__reading:
            DataStorage.__reading = True
            with open(self.__file, 'r') as f:
                DataStorage.__read_data = f.read().splitlines()
        elif DataStorage.__read_linecount == len(DataStorage.__read_data):
            DataStorage.__reading = False
            DataStorage.__read_linecount = 0
            DataStorage.__read_data = None
            return self.read()
>>>>>>> cc3c9b732e35ebdf1dbfa9bde47c0d946a16af0d
        return self.__read_next_line()