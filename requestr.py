import random
from time import time
# for i in range(100):
# 	print time()
xmat = ran = count = 0
for i in xrange(10000000):
	cont = ''
	for x in range(4):
		cont = cont+str(random.randint(1,9999999))[1]

	count = count + 1
	if xmat == cont:
		print xmat
		print "match found"
		print "reqest",count
		break
	xmat = cont
	if i % 10000:
		print "Runnig test"
print "Test completed ....."