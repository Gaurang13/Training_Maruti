import time
start_time = time.time()
def func():
    a,b=1,1
    while 1:
        yield a
        a,b=b,a+b
count=0
for n in func():
    print(n)
    count+=1
    if count==100:
        break
     

end_time=time.time() - start_time
print("%s seconds" % (end_time))


start_time1 = time.time()
list1=[]
a,b=1,1
for i in range(100):
   if a==1:
       list1.append(1)
   else:
       list1.append(a)
   a,b=b,a+b
for i in list1:
    print(i)

        
end_time1=time.time() - start_time1
print("%s seconds" % (time.time() - start_time1))

if end_time>end_time1:
    print("time taken by the generator is more that is=%s",start_time)
else:
    print("time taken by the list is more that is=%s",start_time1)
