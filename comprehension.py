import time
start_list = time.time()
#List comprehension
#simple condition based list
new_list = [i for i in range(1000) if i % 2 == 0]
print(new_list)
end_list = time.time()
list_time = end_list-start_list
print(list_time)




#Dictionary Comprehension
#code to add given two list in other dictionary
number = [1,2,3,4,6,7]
name = ["A","B","C","D","E","F","G"]
new_dict = {k:v for (k,v) in zip(number,name)}
print(new_dict)
# If we take more number and less name than
number = [1,2,3,4,6,7,6]
name = ["A","B","C","D","E","F","G"]
new_dict={k:v for (k,v) in zip(number,name)}#it's condider only matches
print(new_dict) 



#Set Comprehension
#createing simple set using for loop and conditon
start_set=time.time()
new_set = {number for number in range(1000) if number % 2 == 0}
print(new_set)
end_set = time.time()
set_time = end_set-start_set
print(set_time)

 
#generator Comprehension
#example same as list coprehension
start_gen = time.time()
new_gen = (i for i in range(1000) if i % 2 == 0)
for i in new_gen:
    print(i,end = " ")
end_gen = time.time()
gen_time = end_gen - start_gen
print(gen_time)
    
#time comparition between list, set and generator comprehension
dic={
      'lists' : list_time,
      'sets' : set_time,
      'gen'  : gen_time
      }

print(dic)


#size wise comparition between list, set and generatro coprehension
from sys import getsizeof
list_size = getsizeof(new_list)
set_size = getsizeof(new_set)
gen_size =  getsizeof(new_gen)

dic_size = {
        'list' : list_size,
        'set' : set_size,
        'gen_size' : gen_size
        }
print(dic_size)