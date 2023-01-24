def getDivisors(number):
   numDivisors = 0
   for i in range(1, number + 1, 1):
      if number % i == 0:
         numDivisors = numDivisors + 1
   return numDivisors

def trianglular(index):
   return((index *(index + 1)) / 2)

def firstToNDivisors(n):
   i = 1
   while getDivisors(trianglular(i)) <= n:
      i = i + 1
   return trianglular(i)

print(firstToNDivisors(5))
