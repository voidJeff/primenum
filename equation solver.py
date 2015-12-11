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
while a <= len(multiples):
    repeat_ = multiples.count(multiples[a])
    if repeat_%2 == 0:
        b = b * repeat_ / 2
    else:
        b = b * (repeat_ - 1)/2
        factors.append(repeat_)
    
    a = a + repeat_ - 1
print(list(multiples))
print(repeat_)
