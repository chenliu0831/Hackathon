def powerSet(s):
	n = 1 << len(s)

	print []

	for i in range(1,n):
		t = []
		c=0
		while i >0:
			if i &1:
				t.append(s[c])
			c +=1
			i =i>>1

		print t			
		

	
