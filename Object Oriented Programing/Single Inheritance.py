"""
Something about single inheritance:
    1) ek class ko dusre class mai include krna means single inheritance
    2) pahile class ke sare gun jo include kiya hai use lagenge
    3) class class2(class1)  -  syntex of including inheritance
"""
class Chemist:
    def chemistDetails(self, name, yearOfExperiance):
        self.name = name
        self.yearOfExperiance = yearOfExperiance
        print(f"The name of chemist is {name} and the year of experiance is {yearOfExperiance}")


class programmer(Chemist):  #  applying inheritance
    def printProgrammerDetails(self):
        print(f"The name of programer is {self.name} and year of experiance is {self.yearOfExperiance}")
shubham = programmer()

print(shubham.chemistDetails("shubham", 2))  # shubham ko chemist aur programers ke bhi gun lagu hoge kyuki programer mai chemist involve hai
print(shubham.printProgrammerDetails())
