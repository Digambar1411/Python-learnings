for i in range(1,10,2):
  print(i)
print('----------')

for i in range(10,1,-3):
  print(i)
print('----------')


for i in range(1,5):
  print(i)
print('----------')


for i in range(12):
  print(i)
print('----------')


# break, continue, exit 
print('break')
for i in range(10):
  if i == 4:
    break
  print(i)
print('Loop breaked')

print('continue')
for i in range(10):
  if i == 4:
    continue
  print(i)
print('Loop continued')

# print('exit')
# for i in range(10):
#   if i == 4:
#     exit()
#   print(i)
# print('Loop exited')

# Nested for loop
for i in range(1,10,2):
  for j in range(43,11,-11):
    print(i,j)