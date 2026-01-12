for i in range(5):
  for j in range(5):
    print(j,end=' ')
  print(end='\n')

for i in range(5):
  for j in range(5):
    temp = 'A'
    val = ord(temp)
    temp = chr(val + j)
    print(temp,end=' ')
  print(end='\n')

# Hallow square
for i in range(5):
  for j in range(5):
    if i == 0 or j==0 or i==4 or j==4:
      print('*',end=' ')
    else:
      print(' ',end=' ')
  print(end='\n')

# Right angle triangle method 1
print('Right Angle Triangle')
for i in range(5):
  row=''
  for j in range(i+1):
      row+='*'
  print(row,end='\n')
  
# Right angle triangle method 2
print('Right Angle Triangle with spaces')
for i in range(5):
  for j in range(i+1):
    print('*', end=' ')
  print(end='\n')
  
# Hallow Right angle triangle
print('Hallow Right Angle Triangle')
for i in range(5):
  for j in range(i+1):
    if j == 0 or i==4 or i==j:
      print('*', end=' ')
    else:
      print(' ',end=' ')
  print(end='\n')
 
# Equilateral triangle
print('Equilateral triangle')
for i in range(5):
  print(' ' * (5-i-1),end=' ')
  for j in range(i+1):
    print('*', end=' ')
  print(end='\n')

# Equilateral triangle
print('Equilateral triangle')
for i in range(5):
  print(' ' * (5-i-1),end=' ')
  for j in range(i+1):
    if i==4 or j==0 or i==j:
      print('*', end=' ')
    else:
      print(' ',end=' ')
  print(end='\n')