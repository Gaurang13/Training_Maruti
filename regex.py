import re

#findall function
msg="i have to find something new in this pattern"
print(re.findall("in",msg))

#serach method
msg="i have to find something new in this pattern"
print(re.search("in",msg))

#split function
msg="i have to find something new in this pattern"
print(re.split("\s",msg))
print(re.split("\s",msg,2))

#sub function
msg="i have to find something new in this pattern"
print(re.sub("\s","   ",msg))
print(re.sub("\s","   ",msg,3))

#match objects span,string,group
str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.span())
print(x.string)
print(x.group())

#use of special sequence
msg="There is a beautiful parked at road.Some one please call police_100"
print(re.search('\A',msg))
print(re.search('\Ba',msg))
print(re.search('\bat',msg))
print(re.search('The\b',msg))
print(re.findall('\d+',msg))
print(re.findall('\D+',msg))
print(re.findall('\s+',msg))
print(re.findall('\w+',msg))
print(re.findall('\W+',msg))
print(re.findall('100\Z',msg))

#find the ip address from given string using regex
msg="hello 192.168.0.45 and there is many more ip address like 127.0.0.1"
x=re.findall(r"\d+\.\d+\.\d+\.\d+",msg)
print(x)

#finding the email id from given string
msg="hellow dfsadds@gmail.com i am here to help you. my name is jldfjsdl@yopmail.com"
x=re.findall(r"\w+@\w+\.\w+",msg)
print(x)




