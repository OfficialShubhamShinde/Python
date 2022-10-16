"""
Why use args and kwargs:
    1) agar function mai 4 arguments hai aour apne 5 deye to error milega is liye *args or *kwargs ka use kiya jata hai.

args:
    1) args write in *args
    2) args ki jaga kuch bhi name de sakte hai. (*students)
    3)


kwargs:
    1) kwargs write in **kwargs
    2) kwargs ki jaga kuch bhi name de sakte hai. (**age)
    3) ye tuple ho sakta hai list ya dic ho sakte hai.

How use args, kwargs and normal in function:
    1) normal ko start mai use kare warna error milega
    2) bad mai args and kawargs
    3) args or kwargs menditory nahi hai.
"""


# Syntex of normal args and kwargs:
normal = "Name of students are: "
students = ["Shubham", "sakshi", "Rohan"]
dDateAndMonth = {"July": "20", "september": "25", "janewary": "6"}

def func(normal, *students, **dDateAndMonth):  # normal ko last mai nahi likh sakte
    print(normal)
    for items in students:
        print(items)
    for keys, value in dDateAndMonth.items():
        print(keys, value)
func(normal, *students, **dDateAndMonth)
