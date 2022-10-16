# For loop
"""
Something IMP in python:
    1) for loop is write with the help of list, dect, tupple etc.
    2) list ke andar bhi list hogi to bhi wo print krega.
    3) sequence and tabing space is most IMP
syntex of for loop:
for item in list:
    print ("  ")
"""

# Regular for statement (With the help of list)
list1 = [1, 2, 3, 4, 5]
for item in list1:
    print(item)

# for loop in list inside list
list2 = [["shubham", 20], ["sakshi", 25], ["rohan", 6]]
for item in list2:
    print(item);  # jo aitems hai wo as a list print kr dega

# for loop using dictonary inside list
dict1 = dict(list2)
for item, bdate in dict1.items():
    print(item, bdate);

# for loop in tupple
tp = ((1, "s"), (2, "h"), (3, "u"))
for item, names in tp:
    print(item, names)