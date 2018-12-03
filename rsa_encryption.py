from euler_totient_func import gcd, euler_phi_func
import random


# egcd code taken from https://brilliant.org/wiki/extended-euclidean-algorithm/
# overall ref: https://www.lri.fr/~fmartignon/documenti/systemesecurite/6-PublicKey.pdf
def egcd(a, b):
	x,y, u,v = 0,1, 1,0
	while a != 0:
		q, r = b//a, b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
	gcd = b
	return gcd, x, y

# find two 'large' primes
p, q = 53, 23

#compute n = p * q. The hardness assumption is, it's easy to compute n, but hard to find p, q given n. 
n = p * q
phi_n = len(euler_phi_func(n))

# the result of the totient function is actually the multiplication of 
# p - 1 and q - 1, phi(n) = (p-1) * (q-1)

# Select a random integer e, 1 < e < Φ(n), s.t.
# gcd(e, Φ(n)) = 1
e = 3
while True:
	e = random.randint(3, phi_n)
	if gcd(e, phi_n) == 1:
		break


# Compute d, 1< d < Φ(n) s.t. e*d ≡ 1 mod Φ(n), that is:
# find the multiplicative inverse of e, in the group modulo phi_n
# using the Extended Euclidean Algorithm, we can find gcd(a, b) and gcd(a, b) = ax + by
# in the special case where gcd(a, b) = 1, there ax + by = 1 or a | by - 1 => by = 1 mod a
# in this case, a is the phi_n, b is e, so the result of egcd algorithm would return 
# the group inverse of e in the group mod phi_n in the last element as b

d = egcd(phi_n, e)[2]
if d < 0:
	while d < 0:
		d += phi_n

# Now let's say the message is 50. The encryption would be: m^e mod n
# as everyone has the public key e, and n, anyone can encrypt a message with it. 
c = (50 ** e) % n
print('ciphertext c with params: (e, d, phi_n, n, c)', e, d, phi_n, n, c)
# Now to decrypt this ciphertext c, we must use the following formula:
# m = c^d mod n

# and the decryption would be: 
print('decrypted msg is: ', (c ** d) % n) # outputs 50