"""
Caclulates prime factors of a number passed trough argument parameter
"""
import sys


class PrimeFactors:
	def __init__(self):
		self._prime_factors = []


	def __unicode__(self):
		return ','.join(i for i in self.prime_factors)

	def _is_prime(self, n):
		"""
		Retrun true if number is prime
		"""	
		# n has to be a positive integer
		n = abs(int(n))

		# bcs 0 and 1 are not primes we eliminate them
		if n < 2:
			return False

		# except 2 no other even number is prime
		if n == 2:
			return True
		elif not n & 1:
			# by bit masking we determine if n is even
			return False

		for i in range(3, int(n**0.5)+1, 2):
			if n % i == 0:
				return False

		return True


	def all_factors(self, n):
		"""
		Returns all factors of a given number

		>>> PrimeFactors().all_factors(441)
		[[3, 147], [7, 63], [9, 49], [21, 21]]

		"""	
		ret_val = []
		list_len = 0
		i = 2

		while i**2 <= n:			
			list_len = i				
			i += 1		
		
		for i in range(2,list_len+1):			
			if n%i == 0: 			
				ret_val.append(sorted([i,n/i]))

		return ret_val

	
	def get_numbers(self, li):
		"""
		Appends prime factors to an object

		>>> PrimeFactors().get_numbers(441)
		[3, 3, 7, 7]
		"""
		if type(li) != list:
			li = self.all_factors(li)[0]
		
		for i in li:
			if not self._is_prime(i):
				self.get_numbers(self.all_factors(i)[0])
			else:
				self._prime_factors.append(i)
		return self._prime_factors


	def get_prime_factors(self):
		"""
		Retrieves all prime factors
		"""
		return self._prime_factors
	factors = property(get_prime_factors)


	
def main():	
	number = int(sys.argv[1])

	prime = PrimeFactors()
	prime.get_numbers(number)
	print 'Prime factors for %s are %s' % (number, prime.factors)
		

if __name__ == '__main__':
	import doctest
	doctest.testmod()
	main()