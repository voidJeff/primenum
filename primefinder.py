lim = int(input("Set a limit for finding prime numbers "))
num = list(range(2, lim+1))
n = 0
a = 2
while num[n]**2 <= lim:
    while num[n]*a <= lim:
        if num.count(num[n]*a) != 0:
            num.remove(num[n]*a)
        a += 1
    n += 1
    a = num[n]
print(num)
pac = []
for i in num:
    if 600851475143%i == 0:
        pac.append(i)
pac.sort(reverse = True)
print(pac[0])
        
   
    