"""
classes = template
object = instance of the class

Why use oops:
DRY = Do Not Repeat Yourself
"""

# class:
class Student:
    pass  # kuch nahi dalna to pass likhe

shubham = Student()  # object diriving class
Rohan = Student()

# adding components in instance:
shubham.name = "Shubham"
shubham.age = 23
shubham.sub = ["Java", "Python"]
print(shubham.age)
print(shubham.sub)