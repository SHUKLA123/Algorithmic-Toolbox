# Fractional Knapsack Problem in Python


n,W = map(int, input().split(" "))
#l = [(30,5),(20,10),(100,20),(90,30),(160,40)]
l = []
for i in range(n):
	b = tuple(map(int,input().split(" ")))
	l.append(b)
def fractional(n,W,l):
	d = []
	for j in l:
		c = j[0]/j[1]
		d.append((c,j))
	count = 0
	while W > 1:
		if d:
			if int(max(d)[1][1])<=W:
				W = W - max(d)[1][1]
				count = count + max(d)[1][0]
				d.remove(max(d))
			elif max(d)[1][1]>W:
				count = count + max(d)[0]*W
				W = W - max(d)[1][1]
		elif d == []:
			return float("{0:.3f}".format(count))
	return float("{0:.3f}".format(count))
print(fractional(n,W,l))
