"""
Something about comprehensions:
    a) there is list, dictonary, set, generator Comprehensions hoti hai.

"""

# 1) List Comprehensions:
"""Regular Way:
ls = []
for i in range(100):
    if i%3==0:
        ls.append(i)
print(ls)
"""
# Comprehensions Way:
ls = [i for i in range (100) if i%3 == 0]
print(ls)

# 2) Dictionary Comprehensions:
dic = {i:f"item{i}" for i in range(100)}
dic = {value:key for key,value in dic.items()}  # for reverce dictionary values
print(dic)

# 3) set Comprehensions:
# ye value ko ek hi bar leta hai
dresses = {dresses for dresses in ["dress1", "dress2", "dress1", "dress2", "dress1", "dress2"]} # ek hi bar lega
print(dresses)

# 4) Generator Comprehensions:
even = (i for i in range(100) if i%2==0)
print(even.__next__())
print(even.__next__())
