lim = int(input("Set a limit for finding prime numbers "))
num = list(range(2, lim+1))
n = 0
i = num[n]
a = 2
print(2, end="")
while i**2 <= lim:
    while i*a <= lim:
        num.remove(i*a)
        a += 1
    n += 1
    a = i
print(num)
    
