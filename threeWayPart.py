def triWayPart(a):

	s1=0
	s2=0 
	s3=len(a)-1

	while s2 <=s3:
		if a[s2]==2:
			a[s2],a[s3] = a[s3],a[s2]
			s3-=1
		elif a[s2]==0:
			a[s2],a[s1] = a[s1],a[s2]
			s2+=1
			s1+=1
		else:
			s2+=1


