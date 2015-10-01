lim = int(input("Set a limit for finding prime numbers "))
num = list(range(2, lim+1))
i = 2
a = 1
print(2, end="")
while i**2 <= lim:
    while i*a <= lim:
        num.remove(i*a)
        a += 1
    
