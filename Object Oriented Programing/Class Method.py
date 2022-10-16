"""
Something about Class Method:
    1) Class method is used for chage class variable name through a function
    2) is a decorator
"""
class Employee:
    no_of_leaves = 20

    @classmethod
    def change_Leaves(cls, newLEaves):
        cls.no_of_leaves = newLEaves

shubham = Employee()
print(shubham.no_of_leaves)  # original leaves value

shubham.change_Leaves(28)  # as of class method function 28 goes in change_Leaves function and permentaly apply value on variable.
print(shubham.no_of_leaves)  # after changing no_of_leaves value