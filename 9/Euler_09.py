def pythTriplet(sumLessThan):
   for a in range(1, sumLessThan + 1, 1):
      for b in range(a + 1, sumLessThan + 1, 1):
         c = sumLessThan - a - b 
         if (a * a) + (b * b) == c * c:
            return a*b*c, str(a) + ", " + str(b) + ", " + str(c)

print(pythTriplet(1000))