def addStudent():
    numStudent = input("Number of student: ")
    return numStudent

def Student_infor():
    for i in range(numStudent):
        students = {
            "id": input("id: "),
            "name": input("name: "),
            "DoB": datetime.strptime(input( "DoB: "), "%D/%M/%Y"),
        }

def addCourses():
    numCourses = input("Number of courses")
    return numCourses

def Coursese_infor():
    for a in range(Courses):
        courses = {
            "id": input("id: "),
            "name": input("name: "),
        }

def listStudent():
    print('Number of student in class: ')
    print(f'{"ID":^20}{"DATE OF BIRTH":^20}{"NAME":^20}')
    for i in student:
        print(f"{student['id']:^20}{student['dob']:^20}{student['name']:>20}")

def list_courses():
    print('Listing available courses:')

    for course in courses:
        print(f"- [{course['id']}] {course['name']}", end='')
        print(' (marks available)' if 'marks' in course else '')

def show_marks_of_course(course):
    if 'marks' in course:
        print(f"Show marks of the course {course['name']}:")

        print(f'{"NAME":^20}{"MARK":^6}')
        for student, mark in course['marks']:
            print(f"{student['name']:<20}{mark:>6}")
    else:
        print('This course has no marks.')

def select_course_prompt(intro_message):
    list_courses()
    print(intro_message)

    return input('---> Choose a course (Enter nothing to skip): ')

if __name__ == "__main__":
    students = []
    courses = []

    for _ in range(Student_infor()):
        students.append(gStudent_infor())

    for _ in range(Coursese_infor()):
        courses.append(Coursese_infor())
    
    list_students()
    action_loop(msg='Select a course to show marks...', callback=show_marks_of_course)
