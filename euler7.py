from math import floor, sqrt

def prime(n):
        for i in range(2, int(floor(sqrt(n))) + 1):
                if n % i == 0:
                        return False
        return True

num = 2
current_prime = 2
primes = []
while len(primes) < 10001:
	if prime(num):
		primes.append(num)
	num = num + 1
print primes[len(primes) - 1]

