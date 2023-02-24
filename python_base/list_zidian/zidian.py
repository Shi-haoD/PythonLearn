states = {
	'oregen':'OR',
	'Florida':'FL',
	'California':'CA',
	'New York':'NY',
	'Michigan':'MI'
}
#定义键值  对应的关系
cities={
	'CA':'San Francisco',
	'MI':'Detroit',
	'FL':'Jacksonville'
}

cities['NY'] = 'New YorkOne'
cities['OR'] = 'Portland'


print('-1' *10)
print('NY state has :',cities['NY'])
print('OR State has :',cities['OR'])
#键是  cities['NY'] =   值是'New YorkOne'
print('-2'*10)
print("Michigan's abbreviation is : ",states['Michigan'])
print("Florida has avvreviation is :", states['Florida'])
#键是  states['Michigan'] =   值是'MI'
print('-3'*10)
print("Michign has:",cities[states['Michigan']])

print("Florida has :",cities[states['Florida']])
#键是states['Michigan'] 值是MI
# cities[MI] =   值是'Detroit'
print('-4'*10)
for state,abbrev in list(states.items()):
	print(f"{state} is abbreviatied{abbrev}")
#Python 字典(Dictionary) items() 函数以列表返回可遍历的(键, 值) 元组数组。
#把字典用for循环迭代到state,abbrev 两个变量中 ,然后输出了他们键和值 键是state  值是abbrev
print('-5'*10)
for abbrev,city in list(cities.items()):
	print(f"{abbrev} has the city{city}")
#Python 字典(Dictionary) items() 函数以列表返回可遍历的(键, 值) 元组数组。
print('-6'*10)
for state,abbrev in list(states.items()):
	print(f"{state}state is abbreviated {abbrev}")
	print(f"and has city {cities[abbrev]}")
#先取出abbrev的值  再以abbrev的值做键找到对应的值

print('-7'*10)
state = states.get('texas')
if not state:
	print('sorry , no texas.')

city = cities.get('tx','Does Not Exist')
print(f'The city for the state "tx" is "{city}')
#判断值存不存在