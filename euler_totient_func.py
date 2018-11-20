# euler's totient or phi function returns the number of positive integers <= n that are relatively coprime to n

def gcd(a, b):
	# euclid's alg
	if a == 0:
		return b
	if b == 0:
		return a
	return gcd(b, a%b)			

def euler_phi_func(n):
	res = []
	for i in range(1, n+1):
		if gcd(i, n) == 1:
			res.append(i)
	return res			

print(euler_phi_func(1))