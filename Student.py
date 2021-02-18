class Student:

    def __init__(self,name,major,gpa):
        self.name=name
        self.major=major
        self.gpa=gpa

    def isGoodStudent(self):
        if self.gpa>=3.5:
            return True
        else:
            return False

#objects value are being passed through init function(constructor like somehow)

class Triangle:
    def __init__(self,latura1,latura2,latura3):
        self.latura1=latura1
        self.latura2=latura2
        self.latura3=latura3