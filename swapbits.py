def swapbits(x,i,j):
	if (x>>i) & 1 != (x>>j) & 1:
		x = x ^( (1<<i) | (1<<j))

	return x 
