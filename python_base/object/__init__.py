str1 = "aa ee bb cc dd ff ss dda ee ee ss dd ff"
str2 = set(str1.split(" "))
for i in str2:
	print(i,str1.count(i))


