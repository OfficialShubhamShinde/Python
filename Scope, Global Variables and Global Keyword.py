# 1) Local & Global Variables:

# Example:
x = 20  # global Variable
def func1():
    x = 28  # local Variable
    print(x)
func1()

# Explanation:
"""
What is Global, Local Variable:
    1) function ke bher wale x ki value yani global variable.
    2) global aur local me same variable names hoge to function me print kiya huwa variable ki value function ke andar ke variable ki value hogi.
    3) Local variable us function ke liye hi semit hoga.
"""

# 2) Local & Global Keywords:

# Example:
# How to change global variable value:
s = 20
def func2():
    # s = s + 28;  # Aise global variable ko change nahi kr sakte
    global s  # aise global likhe change kr sakte hai.
    s = s + 28
    print(s)
func2()

# Example 3:
# 2 function then what appen about global and local Variable:
def func3():
    z = 2
    def func4():
        global z
        z = 5
    print("Before calling funct4()", z)  # z ko 5 nahi karega kyuki global krne se wo bher dhunde ga na ki dusre func ke andar.
    func4()
    print("After calling func4()", z)
func3()
# Output & Explanation:
"""
1) Error ayega 
2) z ko 5 nahi karega kyuki global krne se wo bher dhunde ga na ki dusre func ke andar.
"""