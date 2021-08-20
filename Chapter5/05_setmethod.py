#Creating amn empty set
a={}
print(type(a))

#Adding value to an empty set 
b=set()
print(type(b))

b.add(4)
b.add(5)
b.add(5)#Cannot add Repeated value in a set
b.add(8)
b.add(9)
#b.add([4,5,6])# Cannt add list list is not hashable
#b.add({4:5})#Cannot add Dictonary
b.add((4,5,6))#We can add tuples in list

#Length of the Set
print(len(b))

#Removal of Item
b.remove(5) # Remove item from set
print(b)

print(b.pop())
print(b)