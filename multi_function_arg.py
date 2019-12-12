
#args
def func(a,*args):
    print(a)
    print(list(args))
func(1,2,4,54,4)

#kwargs
def funce(a,**kwargs):
    print(a)
    print(kwargs.get('first_name'))
funce('xyz',first_name = "gaurang", last_name = "patel")