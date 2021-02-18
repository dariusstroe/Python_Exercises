employeeFile=open("Employees.txt","r")

#print(employeeFile.readlines()[2]) #reading second line in file

for employee in employeeFile.readlines():
    print (employee)

employeeFile.close()