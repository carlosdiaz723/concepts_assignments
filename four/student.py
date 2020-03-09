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
This file contains the Student class which has getters, setters, and a toString
function that allows for easy printing of student information.
'''


class Student():
    '''
    Student class definition
    '''

    # constructor
    def __init__(self, name: str, stuID, numCourses: int):
        # ensure numCourses is an integer
        try:
            numCourses = int(numCourses)
        except TypeError:
            assert type(numCourses) == int, "numCourses must be an integer"
        self.name = name
        self.stuID = stuID
        self.numCourses = numCourses

    # setters
    def setName(self, newName):
        self.name = newName

    def setStuID(self, stuID):
        self.stuID = stuID

    def setNumCourses(self, numCourses):
        self.numCourses = numCourses

    # getters
    def getName(self):
        return self.name

    def getStuID(self):
        return self.stuID

    def getNumCourses(self):
        return self.numCourses

    # toString
    def toString(self):
        return str(self.name + ", ID: " + self.stuID +
                   ", Number of courses: " + str(self.numCourses))
