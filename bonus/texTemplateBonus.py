def multOf(upperBound):
   sum = 0
   for i in range(upperBound - 1, 2, -1):
      if i % 3 == 0 or i % 5 == 0:
         sum = sum + i
   return(sum)
print(multOf(1000))