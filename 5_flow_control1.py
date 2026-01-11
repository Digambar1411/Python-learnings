x= 100
y= 200
z= 30.0
# greatest of three
if x > y and x > z:
  print('x is greatest')
elif y > x and y > z:
  print('y is greatest')
else:
  print('z is greater')

p=10
q=200
r=300
s=600

# Nested and ladder condition

if p < y:
  if q< r:
    if s<r:
      print('s is less than r')
    else:
      if p==100:
        print('p is 100')
      elif p == 200:
        print('p is 200')
      else:
        print('p is neither 100 nor 200')
  else:
    print('second condition false')
else:
  print('first condition false')

# check if number is odd or even

num = 23
if num > 0:
  if num % 2 == 0:
    print('Number is even')
  else:
    print('Number is odd')
else:
  print('Please enter whole number')