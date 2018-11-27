from multiprocessing import Process

class MyProcess(Process):
	def run(self):
		for x in range(5):
			print("执行第%d次"%x)
			
p1 = MyProcess()
p1.start()
