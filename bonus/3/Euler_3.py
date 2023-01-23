def isPrime(num):
   for i in range(2, num // 2 + 1, 1):
      if num % i == 0:
         return(False)
   return(True)

def lrgstPrimeFac(num):
   for i in range(num, 0, - 1):
      if num % i == 0 and isPrime(i):
         return(i)

print(lrgstPrimeFac(13195))
     