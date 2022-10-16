"""
Something about iterable:
    1) Iterable:
        a) Is a object
        b) __iter__() or __getitem__() ye dono method leta hai
        c) string is iterable.
    2) Iterator:
        a) __next__() ye method leta hai.
        a) generator is iterable.
    3) Iteration:
        a) iterate karne ki prakriya ko iteration bolte hai
"""

""" Symply: 
    a) __iter__() ye function run krke iterator generate karega fir uspe __next__() method run karke agle item pradan karega.
    b) Generator is the type of itertor which we can one time traveles.
"""

"""
Range:
    a) range is generator
    for i in range(200):
        print(i)    
"""

"""
Yield: 
    a) Is on the fly value ko generate karega
    b) use in generator
    c) ram bachayega
    d) jab chaiye tabhi run karna 
"""


# define function for iterating generator
def gen(n):
    for i in range (n):
        yield i


g = gen(3)
print(g.__next__())
print(g.__next__())
print(g.__next__())
# print(g.__next__())  # 3 tak hi value hai isliye error dega

# with the help of for loop
for i in g:
    print(i)

# for an iterable:
# str = "shubham"
# str = 1234  error dega kyuki iterable is only on string
itr = iter(str)
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())