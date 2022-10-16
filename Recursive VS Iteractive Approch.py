"""
In Recursion there is two ways to chalculate it:
    1) Interactive Approch
    2) Recursive Approch

Why use Recursion:
    1) It means function ke andar function.
    2) def fun1(n):
            func1(n)  # function ke andar same function nahi likh sakte
       func1(2)
    3) function ke andar same function nahi likh sakte is liye ye do approch use krte hai
"""

# 1) Interactive Approch:
"""
1) Parameterse: param n: Integer
                return: n * n-1 * n-2 * n-3*...1
2) Code logic(Working of Interactive approch for factorial finding)
n! = n * n-1 * n-2 * n-3* ... 1
n! = n * (n-1)
"""
# Syntex:
def fectorial_Interactive(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

inputNumber = int(input("Enter Number Which Fectorial u want to calculate: "))
print("Your Factorial in Interactive Approch is: ", fectorial_Interactive(inputNumber))

# 2) Recursive Approch:
"""
Working of Recursive Approch:
n = 5
5 * fectorial_Recursive(4)
5 * 4 *fectorial_Recursive(3)
5 * 4 * 3 * fectorial_Recursive(2)
5 * 4 * 3 * 2 fectorial_Recursive(1)
5 * 4 * 3 * 2 * 1 = 120
"""
# Syntex:
def fectorial_Recursive(n):
    if n == 1:
        return 1
    else:
        return n * fectorial_Recursive(n-1)

print("Your Factorial in Recursive Approch is: ",fectorial_Recursive(inputNumber))

"""
Which Method is Use (Recursive OR Interactive):
    Recursive:
    1) Recursive problem for debugging.
    2) Easy program write in it.
    Interactive:
    1) Hard but easy to debugging.
    2) but use it.
"""