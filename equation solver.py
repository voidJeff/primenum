i = 2
a = 0
b = 1
num = int(input("Enter the number: "))
multiples = []
factors = []
while i <= num:
    if num % i == 0:
        multiples.append(i)
        num = num / i
    else:
        i += 1
print(list(multiples))
while a <= len(multiples) - 1:
    repeat_ = multiples.count(multiples[a])
    print(repeat_)
    if repeat_%2 == 0:
        b = a * repeat_ / 2
    else:
        b = a * (repeat_ - 1)/2
        factors.append(repeat_)
    
    a += repeat_

print(b)
