# https://code.google.com/codejam/contest/4224486/dashboard#s=p1

for cas in xrange(1,1+input()):
	b, n = map(int, raw_input().strip().split())
	m = map(int, raw_input().strip().split())
	def f(T):
		s = 0
		for i in xrange(b):
			s += (T + m[i]-1) / m[i]
		return s
	
	# find the most time when the number of guests is still less than n
	L = 0
	R = 10**50
	while  R - L > 1:
		M = L + R >> 1
		fM = f(M)
		if fM < n:
			L = M
		else:
			R = M

	# now f(L) < n <= f(R)
	assert f(L) < n <= f(R)
	time_to_available = [0]*b
	for i in xrange(b):
		ct = (L + m[i] - 1) / m[i]
		time_to_available[i] = ct * m[i]
		n -= ct

	assert 0 <= n <= b
	# sort time_to_available by time and id, assign guest to the available one 
	idxs = sorted(range(b), key=lambda i: (time_to_available[i], i))
	print "Case #%s: %s" % (cas, idxs[n-1]+1)