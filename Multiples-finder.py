'''
i = 2
num = int(input("Enter the number: "))
multiples = []
while i <= num:
    if num % i == 0:
        multiples.append(i)
        num = num / i
    else:
        i += 1
print(list(multiples))
'''

multiples = []
lim = int(input("Enter the number: "))
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
b = len(num)
while b >= 0:
    if lim % num[-b] == 0:
        multiples.append(num[-b])
        lim = lim/num[-b]
    else:
        b -= 1
print(list(multiples))        
    