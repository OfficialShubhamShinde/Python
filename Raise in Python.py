"""
1) Rise is working as exception handle
2) There are so much raise in exception please google it and try out
"""

# Raise Exception:
name = input("Enter Your Name: ")
if name.isnumeric():
    raise Exception("Numbers are not allowed")

print(f'Hello {name}')


# Raise ValueError:
value = 20
inputValue = int(input("Enter Value: "))
if inputValue != value:
    raise ValueError


# FileNotFoundError:
openFile = open("Sets.py", "w")
if openFile != True:
    raise FileNotFoundError
