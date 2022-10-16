"""
Syntex:
if x > y:
    print("  ")
else:
    print("  ")

Something IMP:
    1) agar if statement ke bad wale print mai tab itna space nahi hoga to syntex error melega.
    2) 2 bar if hoga ek program mai to ye bar bar chek krta rahega if (her condition check krta rahega) isliye elif ka use kare.

elif:
if x > y:
    print("  ")
elif x == 0:
    print("  ")
else:
    print("  ")
"""

# Example of age:
print("Hey welcome to if elif conditional: \n My age is 23 can i vote?? \n")
age = 23
if age>18:
    print("You can vote")
elif age == 18:
    print("u can also vote")
else:
    print("Y can not vote");

print("\n Thank You")