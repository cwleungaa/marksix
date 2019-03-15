import random

lucky = []

L = [i for i in range(1,50)]

for k in range(1,7):
	s = random.choice(L)
	print('第'+ str(k) +'個中獎號碼是: '+ str(s))
	lucky.append(s)
	L.remove(s)

lucky.sort()

print(lucky)