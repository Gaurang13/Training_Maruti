#simple ternary operator
a,b=39,89
max = a if a > b else b
print("Maximum=",max)

#ternary operator for selecting tuple
a,b,=324,34
print("mimume=",(b,a)[a<b])

#terbary operator for selecting dicsionary
a,b = 34,23
print("minumber=",{True:a,False:b}[a<b])


#nested if-else using ternary operator
a,b=34,554
print("a and b both are equal" if a == b else "a is grater than b" if a > b else "b is gerater than a")