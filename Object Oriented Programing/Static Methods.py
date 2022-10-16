"""
Something about Static Method:
    1) static method kuch nahi bs ek simple function hoga jo print wagera return karega.
    2) is a decorater @staticmethod
    3) na hi class ko argumnet le na ki self ko
"""
class Employee:
    @staticmethod
    def staticMethod(name):
        print(f"hellow {name}. I am Static Method.")
        return "Thank You"

shubham = Employee()
print(shubham.staticMethod("Shubham"))