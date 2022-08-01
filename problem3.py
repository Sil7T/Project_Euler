# Final 

def f(n):
    factor = 2
    while n>1: 
        if n%factor==0:
            yield factor
            n=n/factor
        else:
            factor += 1

primes = f(600851475143)
for item in primes:
    print(f'{item} is a prime factor')

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

# Second Attempt, works for particular question but is not a general solution
'''
def largestprimefactor():
    x = 3
    originalnumber = 600851475143
    while x**2 <= originalnumber:
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

'''


# Third Attempt, a little better but still not able to solve all instances of n

'''
def Euler3(n=16):
    for i in range(2,int(n**(1/2))+1):
        while n % i == 0:
            n //= i
            print(f"Yay, {i} is a factor, now we should test {n}")
            if n == 1 or n == i:
                return i

print(Euler3())
'''