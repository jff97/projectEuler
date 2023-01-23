def isPrime(num):
   for i in range(2, (num // 2) + 1, 1):
      if num % i == 0:
         return(False)
   return(True)

def lrgstPrimeFac(num):
   for i in (primeList(num)).reverse():
      if num % i == 0:
         return(i)

#
def primeList(num):
   list = []
   for i in range(2, (num // 2) + 1, 1):
      if isPrime(i):
         list.append(i)
   return(list)

print(lrgstPrimeFac(131235))