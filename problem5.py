# Attempt 1
'''
def generateprimes():
    number = 2
    originalnumber = 10
    while number < originalnumber:
        for n in range(2,number):
            if number % n == 0:
                number+=1
                break
            else:
                continue
        else:
            yield number
            number+=1


primes = generateprimes()
result = 1
for number in primes:
    result *= number

print(result)
'''

# Attempt 2

numlist=list(range(2,11))
primelist = [2,3,5,7,11]
newlist = []
for num in numlist:
    for n in primelist:
        if num % n == 0:
            newlist.append(num)
            break
print(newlist)

# Attempt 3
""" i = 1
for k in (range(1, 11)): 
    for j in range(1, 11): 
      if (i*j) % k == 0: 
        i *= j 
        break 

print(i)
 """