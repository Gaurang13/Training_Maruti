#Demonstrating use of decorators
def  outer_function(func):
    def inner_function():
        print("First it will call the inner function")
        func()
        print("At last it will call this message")
    return inner_function

@outer_function
def test():
    print("It's between the two messages")

test()

#program to find the exection using decoraters 
import time
import math

def clc_time(func):
    def inner_clc(*args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        print("time taken by {} is {}".format(func.__name__,end_time - start_time))
    return inner_clc
@clc_time
def square_root(number):
    try:
        print(math.sqrt(number))
    except:
        print("please enter the valid input")

square_root(36)