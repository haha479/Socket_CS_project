import time
def testA():
	while True :
		print("---A---")
		yield
		time.sleep(1)
def testB(c):
	while True :
		print("---B---")
		next(c)
		time.sleep(1)
c = testA()
testB(c)