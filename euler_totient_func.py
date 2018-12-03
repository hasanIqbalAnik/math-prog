# euler's totient or phi function returns the number of positive integers <= n that are relatively coprime to n

# recursive euclid's gcd algorithm
def gcd(a, b):
	return a if b == 0 else gcd(b, a%b)

def euler_phi_func(n):
	return [x for x in range(1, n+1) if gcd(x, n) == 1]
