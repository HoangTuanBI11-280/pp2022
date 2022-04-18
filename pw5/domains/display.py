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
        print("\n")