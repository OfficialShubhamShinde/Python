"""
Something about modules:
    1) Pyhton mai built in modules our External modules hote hai.
    2) Statement of use modules:
        import random  ---> import is menditory and then module name.
"""
    # 1) Random Module and its function:
import random
# randint
randInt = random.randint(0, 5)  # 0 se 5 tak koyi bhi random number jenerate karega.
print(randInt)

# random
rand = random.random()  # 0 se 1 tak bidefault konsa bhi dega decimal also included
rand = random.random() * 50  # 0 se 50 tak bidefault konsa bhi dega decimal also included
print(rand)

# choise
list1 = ["Star Pluse", "Set Max", "ABP Maza", "9XM"]
choise = random.choice(list1)
print(choise)


""" How to install External module:
1) Go to terminal in pycharm also 
2) type pip install and module name (pip install sklearn, Panda, etc)
"""

    # 2) Datetime Module function:
import datetime
# today
Date = datetime.date.today()  # today's date show karega
print(Date)

# now
DateTimeAllToday = datetime.datetime.now()  # Todays's date time all
print(DateTimeAllToday)