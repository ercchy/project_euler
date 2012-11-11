import sys

def get_fibonacci(limit):
	ret_val = []
	a, b = 0, 1
	while a <= limit:
		a, b = b, a + b	
		ret_val.append(a)

	return ret_val


def main():
	limit = int(sys.argv[1])

	sequence = get_fibonacci(limit)
	"""
	The Fibonacci series is:

	1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610...

	Now, replacing an odd number with O and an even with E, we get:

	O, O, E, O, O, E, O, O, E, O, O, E, O, O, E...

	And so each third number is even.  We don't need to calculate the odd numbers.  Starting from an two odd terms x, y, the series is:

	x, y, x + y, x + 2y, 2x + 3y, 3x + 5y
	"""
	sum_of_even = sum([i for i in sequence[2::3]])
	print 'Sum of even numbers in Fibonacci sequence is %s' % sum_of_even
	

if __name__ == '__main__':
	main()