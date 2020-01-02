x = 10000000 + 12983*10000
y = 10000000 - 12983*10000
r = 0
for j in range(500):
	for i in range(200000):
		x = x * 5.6800001 / 5.68
	for i in range(100000):
		y = y * 5.6800001 / 5.68
	r = r + x + y
print (r)
