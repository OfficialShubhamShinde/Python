# Map
"""
List mai sare numbers string formate mai hai apko use int formate mai convert krna hai to for loop ki jaga map function ka use kare.
"""
# Example:
# Is a string int converting into int and addition some items.
from functools import reduce

list1 = ["2", "3", "4", "5", "6"]
list1 = list(map(int, list1))
print(list1)
adding = list1[2] + 10
print("Addition of given list is: ", adding)

# Example 2:
# adding fuction work in map function.
def func1(a):
    return a * a

list2 = [1, 2, 3, 4, 5]
print("\nList is : ",list2)
calculating = list(map(func1, list2))
print("Square root of given string with function: ", calculating)

# Example 3:
# Using labda function in map
list3 = [20, 21, 22, 23]
print("\nlist is: ", list3)
usingLambdaInMap = list(map(lambda x: x*x*x, list3))
print("Calculating qube with lambda function: ", usingLambdaInMap)


# Filter:
# function return value mai True return krta ho waha filter function list banata hai.
# Syntex:
list4 = [1, 3, 5, 7, 9]
print("\nGiven List is: ", list4)
def func2(num):
    return num > 3

gr_than_3 = list(filter(func2, list4))
print("Calculated with the help of Filter greater than 3 is: ", gr_than_3)


# Reduce:
# list mai jitne numbers hai unko add krne mai reduce ka use hota hai.
from functools import reduce
list5 = [1, 2, 3, 4, 5]
print("\nGiven List is: ", list5)
addingReduceHelp = reduce(lambda x, y: x+y, list5)
print("Adding content in list using reduce function: ", addingReduceHelp)