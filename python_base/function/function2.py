def add(a,b):
	print(f"加法{a}+{b}")
	return a+b
def sub(a,b):
	print(f"减法{a}-{b}")
	return a-b
def mul(a,b):
	print(f"乘法{a}*{b}")
	return  a*b
def div(a,b):
	print(f"除法{a}/{b}")
	return a/b
print("输入数字进行计算")
aaa = add(500,400)
bbb = sub(30,20)
ccc = mul(40,60)
ddd = div(100,2)
print(f"加法:{aaa},减法:bbb:{bbb},乘法;{ccc},除法{ddd}")

print(add(aaa,sub(bbb,mul(ccc,div(ddd,2)))))
#把所有参数传一遍
#add有两个参数(第一个参数是我们第一次传入aaa计算的结果,第二个参数是第二个方法)以此类推
#分解之后大概是 add(aaa,sub(bbb,2))=add((500+400)+sub((30-20)-2))
#先运行(30-20)-2   结果8 然后是(500+400)+8
print(add(aaa,sub(bbb,2)))
