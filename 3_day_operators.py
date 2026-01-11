# Comparism Conditional Operator
x=20
y=50
print(x<y)
print(x>y)
print(x<=y)
print(x>=y)
print(x==y)
print(x!=y)

# Logical Operators  ( or, not, and)
# not - It is used to reverse (negate) the result of a boolean expression
print('Logical Operator not')
print(not 0)     #is zero a null value - yes
print(not None)  #is None a null value - yes
print(not -99)   #is -99 a null value - No
print(not [])    # Yes
print(not {})    # Yes
print(not True)  # No
print(not False) # Yes

print('Logical Operator or, and')
z=70

print(x<y and x!=y and y>z)
print(x<y and x!=y or y>z)


# swap values without usng 3rd varaible
a=100
b=200

a=a+b 
b=a-b
a=a-b

print(a,b)

# Using 3rd variable
p=10
q=20
print('p,q',p,q)
temp = p
p=q
q=temp
print('p,q',p,q)
 