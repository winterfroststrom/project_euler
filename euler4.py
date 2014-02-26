from math import floor

def palindrome3(n):
	n6 = floor(n / 100000)
	n5 = floor((n % 100000) / 10000)
	n4 = floor((n % 10000) / 1000)
	n3 = floor((n % 1000) / 100)
	n2 = floor((n % 100) / 10)
	n1 = floor((n % 10))
	return n1 == n6 and n2 == n5 and n3 == n4

largest = 0
for i in range(100, 1000):
	for j in range(100, 1000):
		if palindrome3(i * j):
			if i * j > largest:
				largest = i * j
print largest
