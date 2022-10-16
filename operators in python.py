""" Types of operators in python:
    1) Arithmetic operators
    2) Assignment operators
    3) Comparision operators
    4) Logical operators
    5) Membership operators
    6) Bitwise operators
"""

# 1) Arithmetic Operators
# (+, -, *, /, //, **, %)
print ("20 + 28 is", 20 + 28)  # pluse
print ("20 - 28 is", 20 - 28)  # minus
print ("20 * 28 is", 20 * 28)  # multiply
print ("20 / 28 is", 20 / 28)  # divide
print ("20 // 28 is", 20 // 28)  # flore digital
print ("20 ** 28 is", 20 ** 28)  # Exponensial (20 to the power 28)
print ("20 % 28 is", 20 % 28)  # reminder operators

# 2) Assignment Operators
# (=, +=, -=, /=, %=)
x = 20
print(x)  # x ko assign kiya 20 se (x hogaya 20) called assignment operators

# 3) Comparison operators
# (=, +=, -=, %=, !=, <, >, <=, >=)
s=28
print(s <= 20)  # true false return karega

# 4) Logical operators
# (and, or)
a = True
b = False
print(a and b)  # 2 no same ya true ya false hone chaiye
c = True
d = False
print(c or d)  # 2 no mai se 1 same ya true ya false hone chaiye

# 5) Identity Operators
# (is, is not)
z = 20;
y = 28
print(z is y)  # z y hai so false
print(z is not y)  # z ha y nahi so true

# 6) Membership Operators
list1 = [1, 2, 3, 4, 5]
print(20 in list1)  # 20 us list ka part hai ( member hai )

# 7) Bitwise Operators
""" Working with binnary numbers
0 on binary 00
1 on binary 01
2 on binary 10
3 on binary 11
"""
print(0 & 1)  # binnary mai calculation kr ke dega
print(2 | 3)