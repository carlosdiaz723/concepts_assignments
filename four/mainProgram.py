'''
Names / Email:
Carlos Diaz             cdiaz29@students.kennesaw.edu

College of Computing and Software Engineering
Department of Computer Science
---------------------------------------------
CS4308: CONCEPTS OF PROGRAMMING LANGUAGES
SECTION W01 – SPRING 2020
---------------------------------------------
Module 4
Assignment 3


File Description:
This file runs the main loop that adds creates students, adds them to a list,
and prints them out.
'''
# importing the Student class
from student import Student

# create the array of students
arrayOfStudents = list()


def addStudent():
    '''
    method definition for prompting information and adding a student
    '''
    # data gathering
    name = input("Enter student name: ")
    stuID = input("Enter " + name + "'s student ID: ")
    numCourses = input("Enter number of courses for " + name + ": ")

    # create student object
    myStudent = Student(name, stuID, numCourses)

    # change one attribute using setters
    print("\nAdding 1 to the number of courses for ",
          myStudent.getName(), ".", sep='')
    print("Previous number of courses: ",
          myStudent.getNumCourses(), ".", sep='')
    myStudent.setNumCourses(myStudent.getNumCourses()+1)
    print("Number of courses after adding 1: ",
          myStudent.getNumCourses(), sep='')

    # add student into array
    print("\nAdding ", myStudent.getName(), " into the array.", sep='')
    arrayOfStudents.append(myStudent)

    # print array of all students
    print("Updated list of students: ", sep='')
    printAllStudents()


def printAllStudents():
    '''
    method definition for printing student
    array in a visually consistent manner
    '''
    stringToPrint = '{'
    for student in arrayOfStudents:
        stringToPrint += student.toString() + ',\n'
    print(stringToPrint[:-2] + "}")


# start of main code to be ran on script call
# start with adding at least one student
addStudent()

# loop through prompts until no more students left to input
while True:
    answer = input("Add another student? (Y/N)")
    print('\n\n')
    if answer.lower() in ['y', 'yes']:
        addStudent()
    else:
        # once user prompts not to continue, print all students and break loop
        print("Final status of array: ")
        printAllStudents()
        break
