# First Attempt. It works and is fast!

def findpalindrome():
    for x in range(100,1000):
        for y in range(100,1000):
            z = str(x*y)
            if z == z[::-1]:
                yield int(z)
    
palindrome = findpalindrome()

def biggestpalindrome():
    x=0
    for number in palindrome:
        if number>x:
            x=number
    print(x)


biggestpalindrome()