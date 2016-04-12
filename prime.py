import math

max=10000
prime = [2]
print '2 is a prime number.'
for n in range(3, max+1, 2):
	for x in range(2, int(math.floor(n/3)+1)):
		if n % x == 0:
			break
	else:
		prime.append(n)
		print n, 'is a prime number.'
print 'There are', len(prime), 'prime numbers between 1 and', max, '.'