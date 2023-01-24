def lrgstPrimeFac(num):
    list = []
    fac = 2
    while num > 1:
        while num % fac == 0:
            list.append(fac)
            num = num // fac
        fac = fac + 1
    return list
print(lrgstPrimeFac(600851475143))