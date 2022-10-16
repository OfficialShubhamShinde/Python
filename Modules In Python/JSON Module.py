# JSON  = Java Script Object Notation
import json

# loads function:
"""
1) it give string data in same file and exicute.
"""
data = '{"var1":"shubham", "var2":"rohan"}'
# print(data)
parse = json.loads(data)  # parse
print(parse['var1'])


# load Function:
"""
1) is open file and read data on file and print it
"""
loadData = open("dummy.json", "r")
print(json.load(loadData))

# dumps
"""
1) json pyhton mai write krne ka alag tarika hota hai awur acutual me wo javascript mai aur syntex hota hai use parse krne ke liye dumps ka use hota hai
"""
data2 = {
    "website": "x.com",
    "fevFruits": ['Mango', 'Apple', 'watermelon'],
    "fevPlace": ('Iscon Temple', 'Dagdusheth Halwaie Mandir', 'Palange Biryani'),
    "isbad": False
}
dumpsData = json.dumps(data2)
print(dumpsData)


# sort key parameters
"""
1) sort karega increasing and desending order mai jo parameter de gaye hai uske hisab se.
"""
data3 = {
    "age": 23,
    "Roll No": 61,
    "FevLanguage": 1
}
sortData = json.dumps(data3, indent=3, sort_keys=True)
print(sortData)