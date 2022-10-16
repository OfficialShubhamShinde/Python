"""
self = instance
"""
# self:
class Employee:
    def printDetails(self):
        return f"Name is {self.name} and sername is {self.sername}"

shubham = Employee()
shubham.name = 'Shubham'
shubham.sername = 'Shinde'

print(shubham.printDetails())