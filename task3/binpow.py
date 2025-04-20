def BinPow(a, n, f):
	res = a
	n -= 1
	while n:
		if n & 1:
			res = f(res, a)
		a = f(a, a)
		n >>= 1	
	return res
