a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
c=int(input('Enter third number: '))
m=a==b or b==c or c==a
print('Two numbers are equal: ',m)
l=a==b and b==c and c==a
print('Three numbers are equal: ',l)