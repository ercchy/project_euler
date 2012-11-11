
import sys

def main():
	bottom_limit = int(sys.argv[1])
	uper_limit = int(sys.argv[2])
	mod1 = int(sys.argv[3])
	mod2 = int(sys.argv[4])

	naturals = sum([i for i in range(bottom_limit, uper_limit) if i%3 == 0 or i%5 == 0])

	print 'Summary of naturals between %s and %s is %s' % (bottom_limit, uper_limit, naturals)

if __name__ == '__main__':	
	main()