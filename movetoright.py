def MovetoRight(l):
	for i in range(len(l)):
		for j in range(len(l)-1-i):
			if l[j] == 0:
				l[j], l[j+1] = l[j+1],l[j]
	return l

print(MovetoRight([1,0, 5, 3, 0, 2, -1, 0, 5, 6, 7]))
