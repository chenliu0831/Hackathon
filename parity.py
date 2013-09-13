def parity(n):
	p =0

	while n!=0:
		n&=n-1
		p^=1

	return p
