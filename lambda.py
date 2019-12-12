#simple code using lambda
g = lambda x: x+5
print(g(9))

#lambda fuction in  filters
numbers = [10,23432,343,343,5,3432,34,3343,343]
new_number = list(filter(lambda x: (x%2 == 0),numbers))
print(new_number)

#lambda function in map
numbers = [1,2,3,4,5,6,7,8]
new_numbers = list(map(lambda x:x**3,numbers))
print(new_numbers)

#lambda function in reduce
from functools import reduce
numbers = [324,546,56,343,565,43]
sum1 = reduce((lambda x,y:x+y),numbers)
print(sum1)

#lambda function in map
#if we try to put conditon in map function than it will return true or false as a result in list
#output [False, True, False, True, False, True, False, True]
numbers = [1,2,3,4,5,6,7,8]
new_numbers = list(map(lambda x : (x%2 == 0),numbers))
print(new_numbers)


#fibonacci using lambda function
def fibbo(count):
    fib_ser = [0,1]
    list(map(lambda x:fib_ser.append(sum(fib_ser[-2:])),range(2,count)))
    return fib_ser[:count]
print(fibbo(20))