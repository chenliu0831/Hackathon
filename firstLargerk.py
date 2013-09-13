def search1(a,k):
	low = 0
	hi = len(a)-1
	mid =0
	res =-1

	while low<=hi:
		mid = low +( hi-low)/2
		
		
		if a[mid] >k:
			res = mid
			hi=mid-1
		else:
			low=mid+1

	
	return res
