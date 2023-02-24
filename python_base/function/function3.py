def formaula(start_num):
	one = start_num *500
	two = one/1000
	three = two / 100
	return  one ,two ,three
start_num1 = 10000
first , second , third = formaula(start_num1)
print("whith a staring point of{}".format(start_num1))
print(f"we'd have {first} ,{second},{third}")

start_num1 = start_num1/10
formaula = formaula(start_num1)
print("{},{},{}".format(*formaula))