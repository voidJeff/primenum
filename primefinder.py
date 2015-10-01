lim = int(input("Set a limit for finding prime numbers "))
i = 2
a = 1
print(2, end="")
while :
    num += 1
    boov = 0
    if num%2 != 0:                      #if 2 does not divide it
        boov = 0
        while factor < rangenum:
            if num%factor != 0:         #if the current factor does not divide it
                boov += 0
            else:
                boov -= 1
            factor += 1                 #change the testing factor
    else:
        boov -= 1
    if boov == 0:
        print(num)
    rangenum -= 1
