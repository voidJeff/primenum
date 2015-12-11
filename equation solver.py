i = 2
a = 0
num = int(input("Enter the number: "))
multiples = []
while i <= num:
    if num % i == 0:
        multiples.append(i)
        num = num / i
    else:
        i += 1
while a <= len(multiples):
    repeat_ = multiples.count(multiples[a])
print(list(multiples))
print(repeat_)
