from find_group_generator import find_all_group_gen, generate_group_elements
import random

# reference: http://homepages.math.uic.edu/~leon/mcs425-s08/handouts/el-gamal.pdf

# choose a suitable prime, i.e. large enough to hold the message space

p = 17

# Find a group generator for p
G = [x for x in range(1, p)]
generators = find_all_group_gen(G, p)
# take the first one
g = generators[0]

# find a random element in G
x = G[random.randint(0, len(G) - 1)]

# compute h = g^x % p
h = (g**x) % p


# Now choose a msg m and random y both in G. 
m = random.randint(0, p) # could be any value in range(1, p)
y = G[random.randint(0, len(G) - 1)]

# ciphertext (c1, c2) = (g^y, h^y * m)
c1, c2 = (g**y) % p, ((h**y) * m) % p

print('encryption is: (c1, c2)', c1, c2)

# decryption
# plaintext message is: m = c2 / (c1 ^ x) = c2 * c1 ** (p - 1 - x)
print('g =', g,  ', x =', x, ', h =', h, ', m =', m, ', y =', y, )
print('decrypted message: ', (c2 * c1 ** (p - 1 - x)) % p)