import math
def getDivisors(n):
   numDiv = 0
   for i in range(1,math.floor(1 + math.sqrt(n))):
      if n % i == 0:
         if n / i == i:
            numDiv = numDiv + 1
         else:
            numDiv = numDiv + 2
   return numDiv

def trianglular(curNumber, index):
   return(curNumber + index)

def firstToNDivisors(n):
   i = 1
   curTriangle = 0
   while getDivisors(trianglular(curTriangle, i)) <= n:
      curTriangle = trianglular(curTriangle, i)
      i = i + 1
   return trianglular(curTriangle, i)

print(firstToNDivisors(500))