'''
Carlos Diaz
Module 4 -- Assignment 3
'''

from student import Student

arrayOfStudents = list()


def addStudent():
    name = input("Enter student name: ")
    stuID = input("Enter " + name + "'s student ID: ")
    numCourses = input("Enter number of courses for " + name + ": ")
    myStudent = Student(name, stuID, numCourses)

    print("\nAdding 1 to the number of courses for ",
          myStudent.getName(), ".", sep='')
    print("Previous number of courses: ",
          myStudent.getNumCourses(), ".", sep='')
    myStudent.setNumCourses(myStudent.getNumCourses()+1)
    print("Number of courses after adding 1: ",
          myStudent.getNumCourses(), sep='')

    print("\nAdding ", myStudent.getName(), " into the array.", sep='')
    arrayOfStudents.append(myStudent)
    print("Updated list of students: ", sep='')
    printAllStudents()


def printAllStudents():
    stringToPrint = '{'
    for student in arrayOfStudents:
        stringToPrint += student.toString() + ',\n'
    print(stringToPrint[:-2] + "}")


addStudent()
while True:
    answer = input("Add another student? (Y/N)")
    print('\n\n')
    if answer.lower() in ['y', 'yes']:
        addStudent()
    else:
        print("Final status of array: ")
        printAllStudents()
        break
