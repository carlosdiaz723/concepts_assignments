class Student():

    def __init__(self, name: str, stuID, numCourses: int):
        try:
            numCourses = int(numCourses)
        except TypeError:
            assert type(numCourses) == int, "numCourses must be an integer"
        self.name = name
        self.stuID = stuID
        self.numCourses = numCourses

    def setName(self, newName):
        self.name = newName

    def setStuID(self, stuID):
        self.stuID = stuID

    def setNumCourses(self, numCourses):
        self.numCourses = numCourses

    def getName(self):
        return self.name

    def getStuID(self):
        return self.stuID

    def getNumCourses(self):
        return self.numCourses

    def toString(self):
        return str(self.name + ", ID: " + self.stuID +
                   ", Number of courses: " + str(self.numCourses))
