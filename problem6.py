sum_of_square = 0
square_of_sum = 0
for n in range(1,101):
    sum_of_square += n**2
    square_of_sum += n
print(-sum_of_square+square_of_sum**2)