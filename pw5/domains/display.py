<<<<<<< HEAD
from domains.mark import *

class Display:
      def accept(self, id, name, DoB, marksheet ):
        ob = Student(id, name, DoB, marksheet )
        ls.append(ob)

      def display(self, ob):
        print("id   : ", ob.id)
        print("name ", ob.name)
        print("DoB : ", ob.DoB)
        print("marksheet : ", ob.marksheet)
=======
from domains.mark import *

class Display:
      def accept(self, id, name, DoB, marksheet ):
        ob = Student(id, name, DoB, marksheet )
        ls.append(ob)

      def display(self, ob):
        print("id   : ", ob.id)
        print("name ", ob.name)
        print("DoB : ", ob.DoB)
        print("marksheet : ", ob.marksheet)
>>>>>>> cc3c9b732e35ebdf1dbfa9bde47c0d946a16af0d
        print("\n")