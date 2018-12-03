from collections import defaultdict

# we find the generators of a cyclic group formed by F*_p where p is any prime number. 
def generate_group_elements(prime):
	return [x%prime for x in range(1, prime)]

def find_all_group_gen(group_elems, prime):
	d = {k: True for k in group_elems}	
	res = []
	for elem in group_elems:
		d_check = defaultdict(int)

		for i in range(1, prime):
			v = (elem**i)%prime 
			if v in d_check:
				break
			else:
				d_check[v] = True	
		if len(d_check) == prime - 1:
			res.append(elem)
	return res
