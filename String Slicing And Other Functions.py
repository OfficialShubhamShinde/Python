# String Slicing :

str = "I am shubham shinde"  # sabhi jaga yahi string use ho rahi hai.
print(str)  # string ko print kr dega
print("Length of string is : ", len(str))  # sting ke length batayega
print("3 index number is : ", str[3])  # python mai 0 se start hoti hai index to 3 yani 4 0 se leke 3 tak wala character print hoga.
print("index 2 se leke 6 tak : ", str[2:6])  # 2 index se 6 tak print hoge
print("0 se leke 1000 tak : ", str[0:1000])  # yani 0 se 1000 tak ye maf ke=r dega 1000 wala word pure string print
print("One by one character: ", str[0:19:2])  # last wala 2 ek ek charcter chodke print krega
print("One by one bidefault 1 hota hai", str[::])  #  last wala bidefault 1 hota hai pure sting melige
print(str[::-1])  # pure string ulti ho jayegi (Reverce)
print(str[-8:-7])  # ulti counting start hogi

# String Functions:

str2 = "My name is shubham shinde"
print(str2.isalnum())  # space symbols hoge to false warna ture
print(str2.isalpha())  # alpha numeric hoge to true warna false
print(str2.endswith("shinde"))  # end shinde se ho raha hai to true wrna false
print(str2.count("s")) # kitne number pe s ye uska number
print(str2.capitalize())  # pahile lattter ko capital kr dega
print(str2.find("is"))  # uske number milega kitne position pr hai
print(str2.lower())  # pure sting lower case mai ayegi
print(str2.upper())  # pure sting upper case mai ayegi
print(str2.replace("shubham", "rohan"))  # replace krega shubham ko rohan se