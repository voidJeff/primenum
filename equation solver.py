i = 2
a = 0
b = 1
num = int(input("Enter the number: "))
multiples = [1]
under = 1
factors = 1
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
    if repeat_ < 2:
        under = under * multiples[a] 
    else:
        if repeat_%2 == 0:
            b = b * multiples[a] * (repeat_ / 2)
        else:
            b = b * multiples[a] * (repeat_ - 1)/2
            under = under * multiples[a]
    a += repeat_

print({0}"√"{1}).format(b, under)
