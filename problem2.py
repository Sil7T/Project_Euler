
# First Attempt using recursion took forever
'''
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return fib(n-1)+fib(n-2)
    else: 
        print('invalid input')

def fibsequence(n):
    x = 1
    while x < fib(n):
        if fib(x) % 2 == 0:
            yield fib(x)
        x+=1

print(sum(fibsequence(4000000)))

'''

# Second Attempt, much faster


def fib():
    x = 0
    y = 1
    z = 0
    total = 0
    while z<4000000:
        z = x+y
        if z % 2 == 0:
            total += z
        x = y
        y = z

    return total

print(fib())