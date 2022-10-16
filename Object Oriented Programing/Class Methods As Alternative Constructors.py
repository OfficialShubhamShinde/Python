"""
Something About Alternavtive Constructor:
    1) constructor banake "","", ase argument na leke sidha one linner string likhke use object mai convert karna yani Alternative constructor.
    2)
"""
class Employee:
    def __init__(self, name, sername, age):
        self.name = name
        self.sername = sername
        self.age = age

    @classmethod
    def fromSting(cls, string):
        params = string.split("-")  # splite karega "-" se
        return cls(params[0], params[1], params[2])  # pahila argument second and third arrgument

        # One Linner:
        # return cls(*string.split("-"))  one linner for splitting and returning as of two lines given aheade

shubham = Employee("Shubham", "Shinde", 23)
print(shubham.name)

rohan = Employee.fromSting("Rohan-Shinde-19")
print(rohan.name)
print(rohan.sername)
print(rohan.age)
