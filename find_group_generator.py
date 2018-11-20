from collections import defaultdict

# we find the generator of a multiplicative group formed by F*_p where p is any prime number. 
def generate_group_elements(prime):
	return [x%prime for x in range(1, prime)]

def find_group_generator(group_elems, prime):
	d = {k: True for k in group_elems}	
	for elem in group_elems:
		d_check = defaultdict(int)

		for i in range(1, prime):
			v = (elem**i)%prime 
			if v in d_check:
				break
			else:
				d_check[v] = True	
		if len(d_check) == prime - 1:
			return elem
	return None


print(find_group_generator(generate_group_elements(13), 13))	