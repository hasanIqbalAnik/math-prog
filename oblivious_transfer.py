# scenario: sender s has two messages m0 and m1. receiver has one choice bit. 
# s doesn't want r to know both of the messages. r doesn't want s to know her choice bit. 

# the following is based on the hardness of discrete log assumption

# s, r both work on a multiplicative group zp*, with g as the group generator.

# r chooses a secret x, computes p0 = g^x mod p. p1 <- zp* randomly. 
# r sends these two keys to s. 

# s encrypts c0 = enc(m0, p0), c1 = enc(m1, p1). sends c0, c1 to r. 

# r can only decrypt one of these messages.

# the following implementation is based on ElGamal, working on a group z11* with generator 2.
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

# r's private key: 5, public key p0 = 2^5  mod 11 = 10, and p1 = random(z11*) = 9.
# s's messages m0 = 6, m1 = 7

# r sends p0 = 10, and p1 = 9 to sender s.
# s chooses k0 = 3, k1 = 4
# s encrypts according to el gamal (g^k mod p, m * pk^k  mod p)

c0 = [pow(2, 3) % 11, (6 * pow(10, 3)) % 11] # a public key where the secret key is known
c1 = [pow(2, 3) % 11, (7 * pow(9, 3)) % 11] # random public key
print(c0, c1)


# then r decrypts:from c0 = (c1, c2) pair: m = c1^(p - b - 1) * c2 mod p. by FLT, g^(p - 1) = 1

m0 = (pow(c0[0], 11 - 5 - 1) * c0[1]) % 11
m1 = (pow(c1[0], 11 - 5 - 1) * c1[1]) % 11

print(m0) # actual message
print(m1) # just a random element









