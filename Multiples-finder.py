i = 2
num = int(input("Enter the number: "))
multiples = []
while i <= num / 2:
    if num % i == 0:
        multiples.append(i)
        num = num / i
    else:
        i += 1
print(list(multiples))