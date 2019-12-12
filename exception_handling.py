try:
    a,b=1,0
    z=a/b
except(ZeroDivisionError):
    print("exception handled")
finally:
    print("program closesd succefully")

try:  
    raise NameError("Hii") 
except NameError: 
    print ("exception handled:Name Error")
finally:
    print("program closed succefully")

try:
    f=open("/home/mtech/xyz.txt")
except(FileNotFoundError):
    print("exception handled:File Not Found")
finally:
    print("program closed succefully")


#Nested try-except
try:
    f=open("/home/mtech/xyz.txt")
    try:
        a,b=1,0
        z=a/b
    except(ZeroDivisionError):
        print("exception handled")
except(FileNotFoundError):
    print("exception handled:File Not Found")
finally:
    print("program closed succefully")

#else condition with try-except
try:
    a,b=1,2
    z=a/b
except(ZeroDivisionError):
    print("exception handled")
else:
    print("program work fine")
finally:
    print("program closesd succefully")        