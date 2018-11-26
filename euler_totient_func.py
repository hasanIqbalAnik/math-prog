# euler's totient or phi function returns the number of positive integers <= n that are relatively coprime to n

def gcd(a, b):
	# euclid's alg
	if a == 0:
		return b
	if b == 0:
		return a
	return gcd(b, a%b)			

def euler_phi_func(n):
	return [x for x in range(1, n+1) if gcd(x, n) == 1]

print(euler_phi_func(20))