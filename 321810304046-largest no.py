a = int(input("Enter first number: "))
b= int(input("Enter second number: "))
c= int(input("Enter third number: "))
if (a>= b) and (a>= c):
   l= a
elif (b >= a) and (b>= c):
   l= b
else:
   l= c
print("The largest number is", l)