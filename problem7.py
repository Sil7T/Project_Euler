primelist = [2,3,5,7,11,13]

for n in range(2,120000):
    for prime in primelist:
        if n % prime == 0:
            break
        else:
            continue
    else:
        primelist.append(n)        

print(primelist[10000])
        
