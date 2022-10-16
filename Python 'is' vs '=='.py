"""

Differnce Between is or ==:
== - value equality - Two Object have the same value
is - refernce equa;ity - Two references refer to the same object
"""
# For ex:
a = [1, 2, 3]
b = a
print(b == a)  # value same hai.
print(b is a)  # ek hi object se bane hai.

# Task:
x = [1, 2, "21"]
y = [1, 2, "21"]
print(x is y)  # ek object se nahi bane hai is liye false.
