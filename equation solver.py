i = 2
a = 0
b = 1
num = int(input("Enter the number: "))
multiples = []
under = 1
factors = 1
while i <= num:
    if num % i == 0:
        multiples.append(i)
        num = num / i
    else:
        i += 1
while a <= len(multiples) - 1:
    repeat_ = multiples.count(multiples[a])
    if repeat_ < 2:
        under = under * multiples[a] 
    else:
        if repeat_%2 == 0:
            b = b * multiples[a] * (repeat_ / 2)
        else:
            b = b * multiples[a] * (repeat_ - 1)/2
            under = under * multiples[a]
    a += repeat_
if under != 1:
    print("{0}√{1}".format(int(b), under))
elif under == 1:
    print(int(b))
elif b == 1:
    print("√{1}".format(under))
else:
    
