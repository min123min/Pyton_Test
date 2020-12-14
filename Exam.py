list3 = [1,2,[3,4,'hello']]
list3[2][2]="goodbye"
print(list3)

list4 = [5,3,4,6,1]
list4.sort()
print(list4)

d = {'simple_key':'hello'}
# Grab 'hello'
print(d)
d = {'k1':{'k2':'hello'}}
# Grab 'hello'
# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
#Grab hello
# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
#Grab hello