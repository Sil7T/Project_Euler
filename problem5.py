i = 1
for k in (range(1, 11)): 
    for j in range(1, 11): 
      if (i*j) % k == 0: 
        i *= j 
        break 

print(i)