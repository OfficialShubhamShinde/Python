"""
Something with else with for loop:
    1) for loop ke sath else
    2) There is 2 type of for loop:
        a) ek to sare items khatam hoge wo wala
        b) Break mil jaye wo wala(if else condition wala)
    3) Ye lagu sirf pahile wale pe lagu hoga na ki break statement wale pe.
"""

# When Apply:
ls = ["Roti", "Chickn", "Mutton", "Watter"]
for item in ls:
    print(item)
else:
    print("This is else statement")

# When Not Apply:
for item in ls:
    print(item[0])
    break
else:
    print("This is else statement")  # break stement mila isliye else stement nahi run hoga.

# When we use else statement in for loop:
for item in ls:
    if item == "Rotij":
        print("Your item is is list")
        break
else:
        print("This is else stement.")