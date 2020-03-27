def ti(max):
	n = -1
	l = [1]
	while n<max:
		yield l
		m = []
		l = [0] + l
		for i in range(len(l)):
			if i==len(l)-1:
				c = 1
			else:
				c = l[i] + l[i+1]
			m.append(c)
		l = m
		n = n+1


ty = ti(15)

for i in ty:
	print(i)
