from math import floor, sqrt

num = 600851475143
factors = []

def prime(n):
        for i in range(2, int(floor(sqrt(n))) + 1):
                if n % i == 0:
                        return False
        return True

def prime_factors(n):
        factors = []
        for i in range(2, int(floor(sqrt(n))) + 1):
                while n % i == 0:
                        factors.append(i)
                        n = n / i
        return factors

print max(prime_factors(num))

