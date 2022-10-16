"""
Why use Enumertae function:
    1) agar list, tuple, dic mai se one by one items chaiye to iska use hota hai
"""

# Syntex:
list1 = ["Mango", "Apple", "Banana", "coconuts"]
for index, item in enumerate(list1):
    if index % 2 == 0:
        print(item)