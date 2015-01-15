class Student:
    courseMarks = {}
    name = ""
    def __init__ (self, name, family):
        self.name = name
        self.family = family
    def addCourseMark(self, course, mark):
        self.courseMarks[course] = mark
    def average(self):
        counter = 0
        avg = 0
        for value in courseMarks:
            avg = avg + value
            counter +=1
c = Student("John", "family")
c.addCourseMark("80", "Math")
print (c.average)