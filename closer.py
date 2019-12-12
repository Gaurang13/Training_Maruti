#simple code using closer
def outer_func(value):
    def inner_func():
        return value
    return inner_func
if __name__ == '__main__':
    test = outer_func(50)
    print("value =",test())
    
#logfile using closer
import logging
logging.basicConfig(filename="test.log",level = logging.INFO)
def logger(func):
    def logger_inside(*args):
        logging.info("name is {}".format(func.__name__))
        print(func(*args))
    return logger_inside

def add(a,b):
    return a+b
test_function = logger(add)
test_function(3,8)