import os

# how we do with os:
print(dir(os))  # is a object instrospection matlab hum os ke sath kay kay kr sakte hai wo show kr dega.

# current working location:
print(os.getcwd())  #cwh yani (current working directory). abhi ap jis file pe kam kr rahe ho wo kaha hai wo show karega

# change working directory:
# changeDirectory = os.chdir("c://")  #maualy change working directory with the help of chdir function.
# print(os.getcwd())  # after change directory statement.

# f = open("Time Module.py")  # error ayega kyuki c mai wo file nahi hai apne new directory apply kiye hai upper

# which in directory(files, Folders)
print(os.listdir("d://"))  # d mai kay kay folders hai wo show kr dega Jo path dege usme show kr dega
print(os.listdir("c://"))  # c mai kay kay folders hai wo show kr dega

# Create Folder:
# os.mkdir("trail")

# For creating folders inside folder:
# os.makedirs("Dummy/x")

# Rename File:
# os.rename("dummy.txt", "RenamedDummy.txt")

# Envornment Variables:
print(os.environ.get("path"))  # path variable ki location show krega

# Join Function:
# print(os.path.join("c://", "x.txt"))  Join krega c mai x.txt ko. Jada slash hoge to bhi problem nahi ayega.

# Path.exist
print(os.path.exists("c://android"))  # hogi to true wrna false (folder)
print(os.path.isfile("c://dummy.txt"))  # hogi to true wrna false (file)
