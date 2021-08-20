marks1=int(input("Enter the marks of subject 1: "))
marks2=int(input("Enter the marks of subject 2: "))
marks3=int(input("Enter the marks of subject 3: "))

if(marks1<33 or marks2<<33 or marks3<<33):
    print("You are fail beacause you have less percentage")

elif(marks1+marks3+marks2)/3<40:
    print("You are fail beacause total  percentage less than 40")

else:
    print("You  passed")