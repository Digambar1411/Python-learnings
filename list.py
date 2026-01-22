x = [10,20,'string',45,67.89,True,False]

list=[10,20,30,'Apple',True, False,99.88, None]
index=int(input('enter index at which value must be inserted: '))
value = input('enter value to be inserted')
list.append(value)

y = [10,20,'string',45,67.89,True,False]

for i in range(len(y)-1, index, -1):
  temp = list[i]
  list[i]=list[i-1]
  list[i-1]=temp
print('list',list)


for i in range(len(x)//2):
  temp = x[i]
  x[i] = x[len(x)-1-i]
  x[len(x)-1-i] = temp
print(x)

x.append('append')
print(x)
x.insert(1,'wise')
print(x)
x.pop()
print(x)
x.pop(0)
print(x)



z=[16,2,63,4,4,5,5]
print(z)
z.extend([9,78])
print(z)
# z.clear()
# print(z.index(47))

# print(max(x))
z.sort()
print(z.count(4))


x=[101,102,103,104,105,105]
index=int(input('Enter index at which value should be removed: '))
for i in range(index,len(x)-1,1):
  t=x[i]
  x[i]=x[i+1]
  x[i+1]=t
x.pop()
print(x)