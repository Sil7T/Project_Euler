'''
First Attempt
Generate prime numbers
Try dividing the number with all the prime numbers
Did not go well...Works but too slow
'''


'''
def generateprimes():
    number = 2
    originalnumber = 13195
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

for number in primes:
    if 13195%number == 0:
        largestprimefactor = number

print(largestprimefactor)
'''

# Second Attempt

def largestprimefactor():
    x = 3
    originalnumber = 600851475143
    while x**2 < originalnumber:
        if originalnumber%2 == 0:
            originalnumber /= 2
        else:
            if originalnumber%x == 0:
                originalnumber /= x
                x+=2
            else:
                x+=2
    else:
        return originalnumber

print(largestprimefactor())