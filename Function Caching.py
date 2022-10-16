import time
from functools import lru_cache

@lru_cache(maxsize=3)  # last ke 2 ko save karega
def some_work(n):
    #Some task taking n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':  #Main method
    print("Now running some work")
    some_work(3)  # 3 sec ka time lega
    some_work(1)
    print("Done... Calling again")
    some_work(3)  # 2 bar save hone ke bad ye time nahi lega sidha run hoga.
    print("Called again")