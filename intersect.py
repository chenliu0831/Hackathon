import bisect

def intersect(a,b):
	i = 0
	j=0

	
	
	while i < len(a) and j < len(b):
		if a[i]==b[j] and (i==0 or a[i]!=a[i-1]):
			yield a[i]
			i+=1
			j+=1
		elif a[i] > b[j]:
			j+=1
		else:
			i+=1


