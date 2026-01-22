# 1: Special Operator
# in case primitive checks if both have same values
x='apple'
y='apple'
print(x is y)
print(x is not y)

# in case of non primitive check for memory address 
a=[1,2,3]
b=[1,2,3]
print(a is b)
print(a is not b)


# 2: membership operator
print('membership')
x= [1,2,3,4]
print(1 in x)
print(1 not in x)

z=[1,2,3,4,5,[1,2]]
print([1,2] in z)
print([1] in z)
print('------------')
a='100005643634'
b='100005643634'
# 
print(a is b)