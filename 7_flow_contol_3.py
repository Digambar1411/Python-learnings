# Program to find LCM of two numbers 
# x= int(input('enter 1st number:'))
# y= int(input('enter 2nd number:'))

# if x>y:
#   greatest = x
# else:
#   greatest = y
# print(greatest)
# while greatest % y != 0 or greatest % x != 0:
#   greatest+=1
# print('lcm is ', greatest)

# LCM of three numbers
x= int(input('enter 1st number:'))
y= int(input('enter 2nd number:'))
z= int(input('enter 3rd number:'))

if x > y and x > z:
  greatest = x
elif y > z and y > x:
  greatest = y
else:
  greatest = z

while True:
  if greatest % x == 0 and greatest % y == 0 and greatest % z == 0:
    print('LCM is ',greatest)
    break
  greatest+=1

# Fibonanci series
a=0
b=1
print(a,end=' ')
print(b,end=' ')

i = 3
while i<=10:
  c=a+b
  print(c,end=' ')
  a=b
  b=c
  i+=1

# palinmdrom
num = 1222
temp = num
reverse = 0
while temp > 0:
  reminder = temp % 10
  reverse = (reverse * 10 ) + reminder
  temp = temp//10

if reverse == num:
  print(num,'is palindrom')
else:
  print(num,'is not palindrom')