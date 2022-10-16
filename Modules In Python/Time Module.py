"""
Something about time module:
    1) syntex of starting time: initaial = time.time()
    2) syntex of stop time/calculate time: time.time()-initial
    3) time module is use in how time use for exicuting code.
"""

# Finding which loop is fast (for/while):
import time
initial = time.time()
x = 0
while(x<100):
    print("I am while loop")
    x+=1
print("While loop ran in: ", time.time() - initial, "second")

initial2 = time.time()
for i in range(100):
    print("I am for loop")
print("For loop ran in: ", time.time() - initial2, "second")