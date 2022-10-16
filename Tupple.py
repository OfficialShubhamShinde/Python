# IMP : List mai hum change kr sakte values but tupple mai change nahi kr sakte
# For ex:
list1 = [1, 2, 3, 4]
print("Original List: ", list1)
list1[2] = 10
print("Changed list :", list1)
#Tupple mai asie nahi kr sakte

# Mutable = Can change
# Immutable =  Cannot change

# Tupple = ()
# List = []

# Example of tupple
tp = (1, 2, 3, 4, 5, 6, 7)  # writting tupple
print(tp)

# Tupple ko single intiger likhna hai to :
tp2 = (1,)  # , dena padega
print(tp2)

# Another Example (Easyiest way in python):
a = 20
b = 28
# QUESTION : a ko kr do b aur b ko krdo a
# ANS:
a, b = b, a
print(a, b)
