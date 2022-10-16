"""
There are two type of functions:
    1) Built in function
    2) User define function
"""

# Built in:
a = 20
b = 28
c = sum((a, b))  # sum is built in function
print(c)

# User define function:

# Ex 1: (Without function)
def func1():
    print("I am func1()")

func1()  # for exicuting function
print(func1())  # for printing return value

# Ex 2: (With input)
def func2(s, k):
    print("Addition of 20 and k=28 is: ", a+b)
func2(20, 28)

# Ex: 3 (Return value with the help of variable)
def func3(x, y):
    average = (x + y)/2
    return average  # return nahi kiya to none milega
a = func3(20, 28)  # v mai avergae store ho jayega
print(a)
# IMP: Variable ke through return krns chate ho to function mai rteurn statement likhna chaiye.

# DocString :
"""
What is Doc String:
    1) Function ke andar first line mai jo multi line comment hota hai use doc string m=bolte hai
    2) USE: Bahot sare function ho gaye to us perticular function ka kay meen hai ye janne ke liye
"""
# SYNTEX:
def func4():
    """This is Function first its work is ...."""  # is not a multi line comment is a doc string
print(func4.__doc__)  # for printin syntex of doc string