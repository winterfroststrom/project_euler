from math import floor, sqrt

def prime(n):
        for i in range(2, int(floor(sqrt(n))) + 1):
                if n % i == 0:
                        return False
        return True

sum_of_all = 0

for i in range(2, 2000000):
	if i > 2 and i % 2 == 0:
		continue
	if prime(i):
		sum_of_all = sum_of_all + i

print sum_of_all
