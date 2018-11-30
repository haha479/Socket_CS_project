from greenlet import greenlet

def test():
	print("哈哈")

hh = greenlet(test)
hh.switch()


