"""
Something about Decorators:
    1) Function ki functionality ko modify krde
"""
# Syntex of giving one function property to second:
def func1():
    return "I am Function"

func2 = func1()  # func1() ki carbon copy ban gayi creadtedFuncton1() mai
del func1  # agar upar ka func1() delet bhi kare to bhi creadtedFuncton1() run hoga kyuki uski copy ban gayi hai
print(func2)


# Returning function as a function:
def func3(num):
    if num == 0:
        return print
    if num == 1:
        return sum
a = func3(0)
print(a)


# function ke andar function as an argument:
def func4(func5):
    func5("I am function calling inside func4()")
func4(print)


# decorators concept:
def dec1(dumyFunction):
    def functionInsideDecFunction():
        print("Exicuting")
        dumyFunction()
        print("Exicuted")
    return functionInsideDecFunction

@dec1
def whatReturnDummyFunction():
    print("I am good boy")
whatReturnDummyFunction()

""" Optional Line writtingFunc6Syntex() ke upar @dec1 bhi laga sakte hai"""
# writtingFunc6Syntex = dec1(writtingFunc6Syntex)














