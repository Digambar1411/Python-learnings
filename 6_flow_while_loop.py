# while loop example 1
i=1
while i<=5:
  print(i)
  i+=1

# example 2
i=15
x=100
y=56
z=83

while i>11:
  z=z+3
  y=y+2
  x=x+10
  print(i,x,y,z)
  i=i-1

# 5 Table 
i = 1
n=5
while i<=10:
  print(n,'X',i,'=',n*i)
  i+=1

# check number is Prime number
# method 1 
i = 1
n= int(input('Enter number :'))
count=0
while i<=n:
  if n%i==0:
    count+=1
  i+=1
if count == 2:
  print(n,'is prime number')
else : 
  print(n,'is not prime number')


# method 2 (optimised)
i = 1
n= int(input('Enter number :'))
count=0
while i<=n:
  if n%i==0:
    count+=1
    if count > 2:
      isPrime = False
      break
  i+=1
if isPrime:
  print(n,'is prime number')
else:
  print(n,'is not prime number')
