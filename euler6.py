sum_squares = 0

for i in range(1, 101):
	sum_squares = sum_squares + pow(i, 2)

print pow(sum(range(1, 101)), 2) - sum_squares

