"""
What is try and except:
    1) agar error aa raha to wo handel karega string ki taur pe show karega error ko
    2) aur niche wala bhi code exicute hoga
"""

# Syntex:
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

try:  # try karo
    print("The addition of this two number is: ", int(num1) + int(num2))  # ye run krna
except Exception as e: # nahi huwa error aa raha to error ko e ki taur pe string ke taur pe show krwa do
    print(e)  # aur use print krwa do

print("This is IMP Line")  # last wali line ko bhi exicute krwa do