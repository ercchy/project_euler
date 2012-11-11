import sys
import math


def is_palindrom(n):
	"""
	Checkes if number is paindrom	
	"""
	num_to_str = str(n)	
	if len(num_to_str) & 1:		
		return False

	start = num_to_str[0:len(num_to_str)/2]
	end = num_to_str[len(num_to_str)/2:]

	return start == end[::-1]


def find_product(digits_len):
	m = int(''.join(['9' for i in range(digits_len)]))	
	n = m

	limit_m = int(''.join(['9' for i in range(digits_len - 1)]))+1	

	for count_m in range(m,limit_m-1,-1):
		for count_n in range(n,limit_m-1,-1):
			if is_palindrom(count_m * count_n):
				return count_m, count_n, count_m * count_n		
			

def main():

	arg = int(sys.argv[1])
	product = find_product(arg)
	print 'Palindrom %s is the highest number of multiplication '\
		'between %s and %s which is %s number digit' % \
		(product[2], product[0], product[1], arg)


if __name__ == '__main__':
	import doctest
	doctest.testmod()
	main()