def nthPrime(n):
   lastPrime = 2
   i = 2
   while n != 1:
      i = lastPrime + 1
      while not isPrime(i):
         i = i + 1
      lastPrime = i
      n = n - 1
   return lastPrime
def isPrime(num):
   for i in range(2, (num // 2) + 1, 1):
      if num % i == 0:
         return False
   return True
print(nthPrime(10001))