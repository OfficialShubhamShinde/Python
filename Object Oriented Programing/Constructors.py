"""
Something about Constructor:
    1) ap ne dekha instance ko .variable jodke dena padta hai like:
        shubham.name = "Shubham"
    2) ase likhne ki jarurath nahi hai is liyr constructor ka use hota hai.
"""
class Employee:
    def __init__(self, name, sername, age):  # make sure write __init__
        self.name = name
        self.sername = sername
        self.age = age

shubham = Employee("Shubham", "Shinde", 23)
print(shubham.name)
print(shubham.age)
print(shubham.sername)