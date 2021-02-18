from Student import Student
from Student import Triangle

student1= Student("Jim","Business",19,3.1,True)
student2=Student("Darius","Cybernetics",20,4.0,False)

print(student1.name)
print(student1.gpa)
print(student1.isOnProbation)
print(student2.name+" studies "+student2.major+" , is "+str(student2.age)+" years old and has a GPA of "+str(student2.gpa))

def isDreptunghic(l1,l2,l3):
    if l1*l1+l2*l2==l3*l3 :
        print("Triunghi dreptunghic")
    else:
        print("Triunghiul nu este dreptunghic")


triangle1=Triangle(3,4,5)
triangle2=Triangle(1,7,12)

isDreptunghic(triangle1.latura1,triangle1.latura2,triangle1.latura3)
isDreptunghic(triangle2.latura1,triangle2.latura2,triangle2.latura3)
