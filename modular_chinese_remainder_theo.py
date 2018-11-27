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


# select two primes whose product is larger than AB
p1 = 13
p2 = 17


a1 = (A%p1) * (B%p1) % p1
a2 = (A%p2) * (B%p2) % p2


# Calculate M = p1 * p2
M = p1 * p2

# Find M1 = M/p1, M2 = M/p2
M1 = M/p1
M2 = M/p2

# find group inverses of M1 and M2. 


y1, y2, temp = 1, 1, M1
while True:
	if M1 % p1 == 1:
		break
	else:
		M1 += temp
		y1 += 1
M1 = temp		
temp = M2		
while True:
	if M2 % p2 == 1:
		break
	else:
		M2 += temp
		y2 += 1
M2 = temp	
# after finding the group inverses, it's pretty straightforward. 
# the answer x = (a1 * M1 * y1 + a2 * M2 * y2) mod M

print((a1 * M1 * y1 + a2 * M2 * y2 )%M) # correct result