from math import *

def calculate_num_pow(base, pw):
	# check if complex
	if isinstance(pw, complex):
		if pw.real == 0:
			return cos(pw.imag * log(base)) + 1j * sin(pw.imag * log(base)) 
		else:
			return (base**pw.real) * (cos(pw.imag * log(base)) + 1j * sin(pw.imag * log(base))) 
	else:
		return base**pw



def calculate_zeta(s):
	sm = 0
	for i in range(1, 1000):
		v = 1/calculate_num_pow(i, s)
		print(i, v)
		sm += v
	return sm		
		

print(calculate_zeta(-8))


# need to fix for the numbers of the form 0 + ic. value diverges
