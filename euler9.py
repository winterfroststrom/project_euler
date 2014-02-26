from math import floor, sqrt


def number():
	for a in range(1, 1000):
		for b in range(a + 1, 1000):
			for c in range(b + 1, 1000):
				if a * a + b * b == c * c and a + b + c  == 1000:
					return a * b * c
	return 0

print number()
