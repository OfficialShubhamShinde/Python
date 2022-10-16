"""
Something about Lambda Function:
    1) It is also Called anonymous function.
    2) It is one liner function.
    3) Function ko nahi likhna chate but function jaisa worke chate ho to lambda function ka use hota hai
"""
# Syntex:
lambda_Function = lambda x, y: x+y
print(lambda_Function(20, 28))

# Sorting list using lambda function:
list1 = [[99, 20], [28, 2], [3, 11]]
list1.sort(key=lambda x: x[0])
print(list1)