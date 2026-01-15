def isPrime(n,count,i):
  if n%i == 0:
    count+=1
  if i == n : 
      if count == 2:
        print('prime')
      else :
        print('not prime')
      return  
  i+=1
  isPrime(n,count,i)

isPrime(13,0,1)
isPrime(9,0,1)
isPrime(10,0,1)

# LCM Using recursion 

def getLCM(x,y,i=1):
  if x > y :
    greatest = x
  else:
    greatest = y

  lcm = greatest*i
  if lcm % x and lcm %y == 0:
    print('LCM is',lcm)
    return
  i+=1
  getLCM(x,y,i)
getLCM(4,14)


def findSum(x,i=1):
  if i == 11:
    print('sum is',x)
    return
  x=x+i
  findSum(x,i+1)
findSum(10)

def isPrime2(x,i=1,count=0):
  if i == x:
    if count == 1:
      print('prime')
    else :
      print('not prime')
      return
  if x%i==0:
    count+=1
  i+=2
  isPrime2(x,i,count)

def findSum(x,i=1,sum=0):
  sum+=i
  if i==x:
    print('sum is',sum)
    return
  i+=1
  findSum(x,i,sum)
# findSum(10)


def printTable(x,i=1):
  print(x,'*',i,'=',x*i)
  if i == 10:
    return
  i+=1
  printTable(x,i)
# printTable(5)
# printTable(10)
