sum_of_multiples = 0

def arith_seq(delta, start, end):
	return ((end - start) / delta + 1) * (start + end) / 2

print arith_seq(3, 0, 999) + arith_seq(5, 0, 995) - arith_seq(15, 0, 990)
