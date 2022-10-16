# Syntex:
"""
Simple Syntex for open and read file:
f1 = open("dummy.txt")  # target fil which u can read
content = f.read()
print(content)  # for exicutting such a file
f.close()  # menditory to close file
"""

""" read function:
    1) read ke bad () is me jitne character chaiye utne milege
    2) Jitne character chaiye utne string mai hai bada number hai to puri srting hi return hogi our kuch nahi
    3) () is me kuch nahi hoga to bidefault pure string milege
"""
"""
f2 = open("dummy.txt")
print("First three words in file are: ")
threeWords = f2.read(3)
print(threeWords)
f2.close()  # menditory to close file
"""

# Print file with the help of for loop:
""" 
f3 = open("dummy.txt")
for line in f3:
    print(line, end="")

f3.close()  # menditory to close file
"""


# Another way to print file line by line (readline()):
""" 
f4 = open("dummy.txt")
print(f4.readline())  # for print first line 
print(f4.readline())  # for print second line 
f4.close()  # menditory to close file
"""

# Print content of file in list formate:
""" 
f5 = open("dummy.txt")
print(f5.readlines())  # list formate mai return karega
f5.close()  # menditory to close file
"""