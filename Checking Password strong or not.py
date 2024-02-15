#Checking Password strong or not ?
#1 Checking Password have 8 digit or not ?
#2 Checking Password have minimum 3 integer value or not ?
#3 Checking Password have Alphabet  or not ?

#code 
number = input("Enter Your Password :")
result = {}
if len(number) >= 8:
    result["length"] = True
else:
    result["length"] = False
digit = False
for i in number:
    if i.isdigit():
        digit = True
result["digit"] = digit
uppercase = False
for i in number:
    if i.isupper():
        uppercase = True
result["upper-case"] = uppercase
print(result)
print(result.values())

if all(result.values()):
    print("Password is Strong !!")
else:
    print("Password is weak !!")






