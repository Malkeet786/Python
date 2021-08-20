# name=input("Enter your name :") 
# print("Good Afternoon "+ name)

letter = '''Dear <|NAME|>,

                        You are selected!

                        <|DATE|>'''

name=input("Enter your Name\n")
date=input("Enter your Name\n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<DATE>",date)
print(letter)