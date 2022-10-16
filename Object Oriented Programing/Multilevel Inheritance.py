"""
Something about Multilevel Inheritance:

"""

# Syntex
class Dad:
    basketball = 1
    def basketballInfo(self):
        return f"yeh I am playing basket ball at {self.basketball} time."

class Son(Dad):
    basketball = 3
    def basketballInfo(self):
        return f"Yehh Rock!  I am playing basket ball at {self.basketball} time."

class Grandson(Son):
    dance = 5
    def dance(self):
        return f"i am just dancing"

ashok = Dad()
shubham = Son()
x = Grandson()

print(shubham.basketball) # shubham mai basketballl = 3 hai to 3 out put dega warna inherted wala mai se dega.
print(shubham.basketballInfo())  # function ke name same hai to wo inherite kr rahe hai dono mai se ek exicute hoga agr ek nahi higa to