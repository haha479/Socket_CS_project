
import re


def add(num):
	print(num)
	print(num.group())
	strnum = num.group()

	num = int(strnum)+1
	return str(num)


result = re.sub(r"\d+",add,"python : 990 java : 880")
print(result)

print("--"*10)
ret = re.sub(r"\d+",add,"haha :97")

print(ret)