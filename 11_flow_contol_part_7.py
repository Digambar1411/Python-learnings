# Diamond pattern 
for i in range(5):
  print(' ' * (5-i-1),end=' ')
  for j in range(i+1):
      print('*',end=' ')
  print(end='\n')

for i in range(4):
  print(' ' * (i+1),end=' ')
  for j in range(4,i,-1):
     print('*',end=' ')
  print(end='\n')

# Hallow Diamond Pattern
for i in range(5):
  print(' '*(5-i-1),end=' ')
  for j in range(i+1):
    if j==0 or i==j:
      print('*',end=' ')
    else:
      print(' ',end=' ')
  print(end='\n')
for i in range(4):
  print(' '*(i+1),end=' ')
  for j in range(4,i,-1):
    if j==4 or j==i+1:
      print('*',end=' ')
    else:
      print(' ',end=' ')
  print(end='\n')

