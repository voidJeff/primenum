
i = 2
num_ = int(input("Enter the number: "))
multiples_ = []
print("Loading...")
while i <= num_:
    if num_ % i == 0:
        multiples_.append(i)
        num_ = num_ / i
    else:
        i += 1
print(list(multiples_))

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
while b >= 0 and lim > 1:
    if lim % num[-b] == 0:
        multiples.append(num[-b])
        lim = lim/num[-b]
    else:
        b -= 1
print(list(multiples))        
''' 
'''
i = 2
num_ = 6
while num_ < 10:
    multiples_ = [1]
    while i <= num_:
        if num_ % i == 0:
            multiples_.append(i)
            num_ = num_ / i
        else:
            i += 1
    i = 2
    sum_ = sum(multiples_)
    if sum_ == num_:
        print(num_)
    num_ += 1
    

    '''
    
