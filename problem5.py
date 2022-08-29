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
primelist = [2,3,5]
newlist = []
x=0
for num in numlist:
    if num % (primelist[0]) == 0:
        newlist.append(num//(primelist[0]))
        x += 1
    else:
        x += 1
print(newlist)