myDict={
    "Pankha":"Fan",
    "Dabba":"Box",
    "Vastu":"Item"
}
print("Options are",myDict.keys())
a=input("Enter a Hindi words\n")
#print("The meaning of word is :",myDict[a])

#This line will not throw an error
print("The meaning of word is :",myDict.get(a))