# The following code is a simulation of proof. 
# Theorem: There exists two distinct subset of the set [1, 2, 3, 4, 5], whose sum is equal to each other. 
# Because there could be 2^5 = 32 subsets and the maximum sum is less than 5 * 5 = 25, according to the
# pigeonhole principle, there must be at least two subsets whose sum is equal to each other. 

def power_set(s):
	'''return the power set of input set s'''
	if not s:
		return [[]]
	temp = power_set(s[1:])
	res = []
	res.extend(temp)
	for item in temp:
		res.append([s[0]] + item)
	return res

pws = power_set([1, 2, 3, 4, 5])

d = {}

for item in pws:
	if sum(item) in d:
		d[sum(item)].append(item)
	else:
		d[sum(item)] = [item]
print(d)		