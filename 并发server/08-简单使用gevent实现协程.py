import gevent

def test(n):
	for x in range(n):
		print(gevent.getcurrent(),x)
		#写一个耗时操作,协程在运行的时候碰见了耗时操作就会切换另一个协程执行
		#不写效果不一样
		#协程中休眠使用如下这种
		gevent.sleep(0.5)

gevent.joinall([
gevent.spawn(test,5),
gevent.spawn(test,5),
gevent.spawn(test,5)
])
