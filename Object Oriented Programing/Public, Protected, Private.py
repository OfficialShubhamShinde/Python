"""
Something about Public, Protected, Private:
    1) Public:
        a) Public yani kaise bhi acsess kr sakta hai, koyi bhi dekh sakta hai
        b) Variable ko Public kr ne ke liye kuch nahi  kr na padta name as it is likhe
        c) Syntex: public = 3

    2) Protected:
        a) koyi ek insan dekhega kuch lig dekhege matlab privacy type
        b) Syntex: _protected = 2
        
    3) Private:
        a) Private ko koyi assess nahi kr sakta wo us class ke liye hai use banayi gari class ko ki dekhega.
        b) syntex: __private = 20
        c) for giving output: print(instance_name.class_name.privatevariablename)
"""
# Syntex:

class exploringPublicPrivateProtected:
    public = 10
    _protected = 19
    __private = 20
    def dummy(self):
        return f"I am dummy function"

print(exploringPublicPrivateProtected.public) # for accessing Public variable
print(exploringPublicPrivateProtected._protected) # for accessing Protected variable

accessingPrivateVariable = exploringPublicPrivateProtected()
print(accessingPrivateVariable._exploringPublicPrivateProtected__private) # for accessing private variable

