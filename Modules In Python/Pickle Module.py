"""
Something about Pickle:
    1) Pickle yani ek .pkl file mai onject ko store krna
    2) object kuch bhi so sakta tupple, string, list etc.
    3) wb for write binary & rb for read binary
    4) retriving ke liye load function ka use hota aur save ke liye dump ka.
    5) is not secure, can not save data in pickle.
    6) is a inbuilt function, pkl file converts in txt but in this sentax is binary.
"""

import pickle

# For creating pickle file:
carList = ["Audi", "BMW", "Farrari", "Honda City"]
pickleFile = open("dummyPickleFile.pkl", "wb")
pickle.dump(carList, pickleFile)
pickleFile.close()

# For retriving pickle file:
pickleFileForRetriving = open("dummyPickleFile.pkl", "rb")
lodingFile = pickle.load(pickleFileForRetriving)  # load use for retriving data from file
print(lodingFile)
print(type(lodingFile))  # type showing