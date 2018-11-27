# multiply two very large integers using polynomials. 

# we can break up the integers into smaller pieces using modular arithmatic and then
# solve the system of congruence equations using chinese remainder theorem to find out 
# the original result of multiplication. Below, a very simple example is presented: 

# step 1: find some primes whose multiplication would be larger than the given numbers' product. 
# calculate Ai mod Pi for all input Ais and primes Pis. 

# AB mod pis =  ((A mod pi) * (B mod pi)) mod pi -- these are the system of congruences 

# two very(?) large integers A and B
A = 12
B = 15


# select two primes whose product is larger than A*B
p1 = 13
p2 = 17


#find ais for all A, B and primes
a1 = (A%p1) * (B%p1) % p1
a2 = (A%p2) * (B%p2) % p2


# Calculate M = p1 * p2
M = p1 * p2

# Find M1 = M/p1, M2 = M/p2
M1 = M/p1
M2 = M/p2

# find inverses of M1 in group Z_p1 and M2 in group Z_p2. 
y1, y2, = 1, 1,

while True:
	if (M1 * y1) % p1 == 1:
		break
	else:
		y1 += 1

while True:
	if (M2 * y2) % p2 == 1:
		break
	else:
		y2 += 1

# after finding the group inverses, it's pretty straightforward. 
# the answer is using CRT: x = (a1 * M1 * y1 + a2 * M2 * y2) mod M

print((a1 * M1 * y1 + a2 * M2 * y2 )%M) # correct result: A*B