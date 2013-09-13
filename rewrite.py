def rewrite(L,M):
	lkt = {}

	for m in M:
		try:
			lkt[m]+=1
		except KeyError:
			lkt[m] =1

	for l in L:
		try:
			lkt[l]-=1
			if lkt[l] < 0:
				return False
		except KeyError:
			return False
	return True
