"""
1) Dictionary is a mapping key pairs
2) Dictionary item, key names are case sensitive
3) Dictionary write in {}
4) We can Dictionary in dictionary

Syntex of Dictionary:
dic = {"Shubham": "apple", "Rohan":"Mango"}
"""

dic = {"Shubham": "Apple", "Rohan": "Mango", "Sakshi": "Strawbery", "Aniket": "Banana"}
print(dic)

# Another Example (Dictionary inside Dictionary)
dic2 = {"Savita": {"Sadi": "lattest", "gaun": "designed"}, "Ashok": "Pants", "Vijay": "TShirts", "Rani": "Dresses"}
print(dic2)

print(dic2["Savita"])  # savita wali dic print hogi

dic2["shalan"] = "nind"  #  ading in Dictionary
print("Affter adding shalan in dic :", dic2)

# del dic2["x"]  # for deleting on Dictionary


# Some functions in Dictionary
dic3 = {"x": 1, "y": 2, "z": 3}
print(dic3)
dic4 = dic3.copy()
print(dic4)  # copy ban gayi dic3 ke dic4 mai

print(dic3.get("x"))  # for getting key value pair of it

dic3.update({"a" : 4})  # updating in that Dictionary
print(dic3)

print(dic2.keys())  # printing key pairs in that Dictionary
print(dic2.items())  # printing Items  in that Dictionary