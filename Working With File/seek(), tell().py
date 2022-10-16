"""
tell():
    1) jo line jana chate ho ki file mai se konse character number se start ho rHI Hi to tell() number ka use kare
    2) For ex:
        f = open("x.txt")
        print(f.readline())
        print(f.tell())
        f.close()

seek():
    1) apko file maise 10 number se jo writte kiya hai wo chaiye to seek function ka use kiya jata hai
    2) for Ex:
        f = open(x.txt)
        print(seek(10)
        print(f.readline())
        f.close()
    3) file content - abcdefg
        seek(3)
        output - defg
"""

# tell():
f = open("dummy.txt")  # open those file u want to
print("starts with character number: ", f.tell())  # starts at
print(f.readline(), end="")  # first line in this file
print("Ends with character number: ", f.tell())  # ends at
f.close()   # menditory to close it

# seek():
f2 = open("dummy.txt")  # open file
f2.seek(11)  #  first 11 character chodke print hoga
print(f2.readline())
f2.close()  # menditory to close it
