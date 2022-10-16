class Employee:
    no_of_leaves = 20  # class Variable

shubham = Employee()  # shubham is a instance
Rohan = Employee()

print(shubham.no_of_leaves)
print(Rohan.no_of_leaves)
print(Employee.no_of_leaves)

""" 
1) no_of_Leaves ko shubham or rohan ke through change nahi kr sakte
2) use change krne ke liye Employee class se he change krna padega:
"""
Employee.no_of_leaves = 28
print("Changed no_of_nodes is: ", shubham.no_of_leaves)

# printing all attributes of instance and class:
print(Employee.__dict__)
print(shubham.__dict__)
print(Rohan.__dict__)