num=int(input("Enter the number:"))
print=False

for i in range(2,num):
    if(num%i==0):
        prime=True
        break

if prime:
    print("The number is prime")
else:
    print("This is not prime")
