class Student:
    def __init__(self,fullname):

        self.name = fullname
        print("Called automatically")

s1 = Student("Jeet")
print(s1.name)

s2 = Student("Harsh")
print(s2.name)
