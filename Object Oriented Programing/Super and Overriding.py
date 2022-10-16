"""
Overriding:
    1) Kise bhi ek function, Constructor, ClassVariable ko use nam se dusri bar likha jaye to use overrriding bolte hai.
    2) Jo second time likha gaya hoga wahi exicute hoga first wala 0 ke barabar ho jayega.
    3) IDE Mai jo override huwa hai wo side mai o^| aise ayega

Supper:
    1) agar overriding karke jo hume pahile wale kho diya hai use lane ke liye super ka use hota hai
    2) override krke bhi exicute krna chate hot to supper ka use hota hai.
"""
# Syntex:
class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    classvar1 = "I am in class B"

    def __init__(self):
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"

        super().__init__()  # supper method
        print(super().classvar1)


a = A()
b = B()

print(b.special, b.var1, b.classvar1)