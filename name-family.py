class Student:
    courseMarks = {}
    name = ""
    def __init__ (self, name, family):
        self.name = name
        self.family = family
    def addCourseMark(self, course, mark):
        self.courseMarks[course] = mark
        return
    def average(self):
        counter = 0
        avg = 0
        for key, value in self.courseMarks.items():
            avg = avg + int(value)
            counter +=1
        avg = avg / counter
        return avg
c = Student("John", "family")
c.addCourseMark("Math", "80")
c.addCourseMark("Science", "70")
c.addCourseMark("English", "90")
print("Family", c.family)
print("Name", c.name)
print(c.average())