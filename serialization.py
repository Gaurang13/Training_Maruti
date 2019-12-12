from sys import getsizeof
#Writing and reading file using json

import json
data = {"first_name": "xyz","last_name": "pqr"}
with open("/home/mtech/file.json",'w') as f:
    data = json.dump(data,f,sort_keys=True)
    print(getsizeof(data))

with open("/home/mtech/file.json",'r') as f:
    data1 = json.load(f)
    print(data1)


#data serialization using pickle

import pickle
data = {"first_name" : "xyz","last_name" : "pqr"}
ser_dump = pickle.dumps(data)
print(ser_dump,getsizeof(ser_dump))

ser_load = pickle.loads(ser_dump)
print(ser_load)