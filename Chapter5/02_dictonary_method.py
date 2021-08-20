myDict={
    "fast": "In a Quick Manner",
    "malkeet": "A Coder",
    "marks":[1,5,7],
    "anotherDict":{'Malkeet':'Player'},
    1:2
}


#Dictonar method
# print(myDict.keys()) # Print the Dictonary Keys
# print(type(myDict.keys())) #Print  class of key
#print(myDict.items()) # Print (key,value) content of item
#print(myDict.values()) #Print the value of keys

print(myDict)
updateDict={
    "vaibhav":"Friend",
    "abhishek":"Friend"
}
myDict.update(updateDict) #update Dictonary
print(myDict)

print(myDict.get("malkeet2"))# Return None as Malkeet2 not present
print(myDict["malkeet2"])#throws error as Malkeet2 not present