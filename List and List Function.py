# How to write list :
list1 = ["Mango", "Apple", "Banana"]  # is a List
print(list1)
print(list1[1])  # list 0 se start hoti hai 1 wala number show krega


# sort, reverce, append, insert, remove, pop, etc functions:
list2 = [4, 5, 3, 1, 2]
print("Original List is: ", list2)
print("Length of list is: ", len(list2))  # length of list

list2.sort()  #  increasing order
print("sorted list is: ", list2)

list2.reverse()  # list reverse hogi
print("Reverse list is: ", list2)

list2.append(10)  # end mai jod do
print("Appending 10 at end: ", list2)

list2.insert(2, 20)  # 2 position mai 20 add hoga
print(list2)

list2.remove(3)  # konsa number delet krna hai
print(list2)

list2.pop()  # last wala hatega
print(list2)


# Slicing list
list3 = [20, 28, 26, 23, 32, 25, 22]
print(list3)

print(list3[:])  # bidefault pure string lega
print(list3[2:5])  # 2 se leke 5 tak
# IMP: Slicing mai original string change nahi hoti baki sorting reverse jaise function mai change hoti hai
print(list3[::2])  # one by one print hoga
print(list3[::-1])  # ulti hogi string
print(max(list3))  # maximum vale
print(min(list3))  # minimum value
