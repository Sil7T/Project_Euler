# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
i = 1
for factor in range(1, 21): 
  for j in range(1, 21): 
    if (i*j) % factor == 0: 
      i *= j
      break 

print(i)

