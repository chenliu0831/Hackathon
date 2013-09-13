import heapq

def mergeFiles(*iterables):
	res =[]

	for itnum, it in enumerate(map(iter,iterables)):
		next = it.next
		
		res.append([next(),itnum,next])

	
	heapq.heapify(res)

	while 1:
		try:
			while 1:
				v,itnum,next = s =res[0]
				yield v
				s[0] = next()
				heapq.heapreplace(res,s)
		except StopIteration:
			heapq.heappop(res)
		except IndexError:
			return	
