#use of partial fuction
from functools import partial
def multi_sum(a,b,c,d,e):
    x= a*2 + b*3 + c*4 + d*5 + e*6
    return x

temp_func = partial(multi_sum,1,2,3)
print(temp_func(4,5))