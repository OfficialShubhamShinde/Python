# Syntex of writting file:
f1 = open("dummy2.txt", "w")  # w for write mode
f1.write("I am file dummy2 created with the help of write function \n")  # adding content on file
f1.close()  # menditory to close file

# Syntex of append:
f2 = open("dummy2.txt", "a")
f2.write("Thank You")
f2.close()

# How many characters in this file we can added:
f2 = open("dummy2.txt", "a")
a = f2.write("Thank You")  # adding how many characters in file (thank you)
print(a)
f2.close()

# Some therotically:
""" 
    1) Write: kuch add krdo file mai
    2) Append: Jo file mai hai uske end mai kuch append kr do add kr do
"""