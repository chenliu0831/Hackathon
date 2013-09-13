def mergeTwosortedlist(l1,l2):
	res=[]

	i1=0
	i2=0

	while i1<len(l1) and i2 <len(l2):
		if l1[i1] <=l2[i2]:
			res.append(l1[i1])
			i1+=1
		else:
			res.append(l2[i2])
			i2+=1

	while i1<len(l1):
		res.append(l1[i1])
		i1+=1
	while i2<len(l2):
		res.append(l2[i2])
		i2+=1

	return res
