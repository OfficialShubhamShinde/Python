# Finally:
"""
    1) finally use for code cleanup(file try mai open ho y ana ho finally maiuse close hona hi hai)
    2) try aur exception run ho ya na ho finally run hoga
"""
try:
    open("x.txt")
except Exception as e:
    print("Error is: ", e)
finally:
    print("Its Finally Statement(Run anyway)")

print("IMP LINE")


# Else:
"""
    1) except run hoga to else nahi run hoga
    2) except run nahi huwa to else run hoga
"""
try:
    f = open("existFile.txt")  # ye file exist krne chaiye
except Exception as e:  # to ye run nahi hoga
    print("Error Is: ", e)
else:
    print("I am else statement.")  # but ye run hoga


# Finally + Else:
"""
Chaye try, excepti, else run ho ya na ho finally run hoga
"""
try:
    f = open("existFile.txt")
except Exception as e:
    print("Error Is: ", e)
else:
    print("I am else statement.")
finally:  # finally statement
    print("I am finally statement")