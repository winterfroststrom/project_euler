sum_of_evens = 0
fib_previous = 1
fib_current = 1
while fib_current < 4000000:
	if fib_current % 2 == 0:
		sum_of_evens = sum_of_evens + fib_current
	fib_current = fib_current + fib_previous
	fib_previous = fib_current - fib_previous

print sum_of_evens
