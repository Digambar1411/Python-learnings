# x= input('enter value: ')
# print(x)

# implicit typecasting : Python automatically convert one data types into another
a = 14
b = 2
c = a/b
print(c, type(c))

# Explicit type casting : We manually convert one data type to other
# y = int(input('Enter Number: '))
# print(float(y))

p = '123'
q = float(p)
print(type(p))
print(type(q))

print('5'+'45')

x = '167.5'
print(int(x)) # Error : int can convert only whole numbers written in string, int except string like '7', '-8', '0'
print(int(float(x))) # Works: float convert string to floting number, then int converts float to int