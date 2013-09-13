
ms = []

def push_max(s,e):
	s.append(e)

	if not ms or e>ms[-1][0]:
		ms.append([e,1])
	elif e == ms[-1][0]:
		ms[-1][1]+=1

	
def pop_max(s):
	if not s:
		e = s.pop()

		if e == ms[-1][0]:
			ms[-1][1]-=1
			if ms[-1][1] == 0:
				ms.pop()

def smax():
	if not ms:
		return ms[-1][0]
