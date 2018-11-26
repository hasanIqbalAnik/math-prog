# let's say we have a secret number. we want to distribute number among a group of people in such a way
# that only by coming at least m them together, can they retrieve that secret number. 

# for example: the number is: 9826521405
# we would divide it into m pieces, in this case, let's say m = 5

# a0 = 98, a1 = 26, a2 = 52, a3 = 14, a4 = 05

# we would build a polynomial by using these ai's as coefficients. 

# f(x) = a4x4 + a3x3 + a2x2 + a1x + a0

# we evaluate this polynomial at n > m distinct points. n would be the number of people we would like 
# to share the secret with. 

import numpy as np

# represent the polynomial in coefficients form
secret_poly_coeffs = np.array([5, 14, 52, 26, 98])

# for each of these points, we would calculate f(x)
eval_xis = np.array([3, 8, 6, 5, 2, 1, 9]) 

# create the vandermode matrix to help with the evaluation
vandermonde = np.vander(eval_xis, len(secret_poly_coeffs))

# evaluation result points
eval_yis = np.matmul(vandermonde, secret_poly_coeffs).reshape(len(eval_xis), -1)


# Now, given these xi's and f(xi)s, we can get back the original coefficients,which is actually the 
# secret number. the interpolation process proceeds as follows
 
print(np.matmul(np.linalg.inv(vandermonde[:-2]), eval_yis[:-2])) # ignore last two rows to make it a square