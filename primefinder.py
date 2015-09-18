rangenum = int(input("Set a limit for finding prime numbers "))
factor = 1
num = 1
booo = 0
while rangenum > 0:
    factor += 1
    num += 1
    if num%factor == 0:
        booo = 0
    else:
        booo = 1
    if booo == 1:
        print(num)
    rangenum -= 1
