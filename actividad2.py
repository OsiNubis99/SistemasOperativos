import sys
from threading import Thread

x = 10000000 + int(sys.argv[1])*10000
y = 10000000 - int(sys.argv[1])*10000
r = 0


class ThreadWithReturnValue(Thread):
	def __init__(self, group=None, target=None, name=None,args=(), kwargs={}, Verbose=None):
		Thread.__init__(self, group, target, name, args, kwargs)
		self._return = None
	def run(self):
			self._return = self._target(*self._args,**self._kwargs)
	def join(self):
		Thread.join(self)
		return self._return
def ciclox(x):
	for i in range(200000):
		x = x * 5.6800001 / 5.68
	return x
def cicloy(y):
	for i in range(100000):
		y = y * 5.6800001 / 5.68
	return y

for j in range(500):
	hilo=ThreadWithReturnValue(target=ciclox, args= (x,))
	hilo.start()
	hilo2=ThreadWithReturnValue(target=cicloy, args= (y,))
	hilo2.start()
	x=hilo.join()
	y=hilo2.join()	
	r=r+x+y
print (r)