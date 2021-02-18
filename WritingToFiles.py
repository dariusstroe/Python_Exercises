# "r" = read
# "w" = write
# "a" = append(adauga)
# "r+"= read & write

employeeFile=open("Employees.txt","w")

employeeFile.writelines("\nKelly- Customer Service")

employeeFile.close()