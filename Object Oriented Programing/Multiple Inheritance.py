class programmer:
    var = 8
    def printProgramerDetails(self, name, language):
        return f"The name of programmer is {name} and language is {language}"

class gymTranee:
    var = 9
    def printGymTrainneDetails(self, name, joiningDate):
        return f"The name is {name} and joining date is {joiningDate}"

class programmerAndGymtranee(programmer, gymTranee):
    # var = 10  # ye var yaha hoga to iski value lega warna inheritance wale first argument ki lega
    pass


shubham = programmerAndGymtranee()  # upar wale 2 no classes ko add krega
print(shubham.printProgramerDetails("Shubham", "JAVA"))
print(shubham.printGymTrainneDetails("Shubham", "20-07-1999"))

print(programmerAndGymtranee.var)




















