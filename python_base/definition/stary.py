#元祖
#print('元祖开始')
# tuple = ('ab',111,'bb',222,1.2)
# tinytuple = (123,'aa')
# print(tuple)
# print(tuple[0])
# print(tuple[1:3])
# print(tuple[2:3])
# print(tuple[2:])
# print(tinytuple * 2)
# print(tinytuple+tuple)
# print('元祖结束')



# print('set集合开始')
# student = {'tom','jock','zhenni','mary','rose'}
# print(student)
# if 'rose' in student:
#     print('rose在集合')
# else:
#     print('rose不再集合zhong')
# a = set('ascd')
# b = set('efgh')
# print(a)
# print(a-b)
# print(a|b)
# print(a^b)



# dict = {}
# dict['one'] = '1-可以'
# dict[2] = '2-可以'
# tinydict = {'name': '刘世豪' , 'id':1 , 'site' : 'www.wocao.com'}
# print(dict['one'])
# print(dict[2])
# print(tinydict)
# print(tinydict.keys())
# print(tinydict.values())

#循环字符串
# a = 'asdsadsa'
# for i in a :
#     print (end=i)

#循环列表
# a =[1,2,3,4]
# for i in a :
#     print(i)

'''按照字符串控制循环次数'''
# import random
# a = 'asdsadsa'#字符串个数为8 循环8次  i == 5 也没用  字符串不能和数字进行比较直接忽略
# for i in a:
#     print(random.randint(1,10))
#     if i == 5:
#         break
# '''使用循环测试列表'''
# asd = ['六十','撒旦撒','撒打啥的阿斯顿是算','撒倒萨撒旦撒','撒旦撒旦撒']
# for i in asd:
#     print(i, len(i))#len方法输出一个列表中元素的长度
# #                     #如果len方法里面是列表名  则输出列表长度

# ss = 'aaa'
# print('shuru')
# while True:
#     if ss == input():
#         break
#     print('输入错误')
# print('成功')

# for i in range(10):
#     if i%2!=0:
#         print(i)
#         continue
#     i+=2
#     print(i,'aaa')
"""List方法"""
# list1 =[123 , 234 ]
# list2 =[123, 345]
# list1 *=5
# print(list1 == list2)
# print(dir(list))    #list里常用的方法
# print(list1.count(123))     #计算元素出现次数
# print(list1.index(123,4,6)) #返回索引位置  例 从4开始都6  123这个元素出现在第几个
# print(list1.reverse())   #反转列表



'''list排序'''
# list1 = [1 , 6 , 4 , 32 , 44 ,31 ]
# for i in list1:
# 	print(i)
# print(list1)
# print(list1.sort())#列表元素从小到大排列
# print(list1)
# list1.sort(reverse=True)  #直接倒序排列列表
# print(list1)
# print(list1.reverse())#想从大到小拍需要sort排完之后在用反转方法返回
# print(list1)
#
# list2 = list1[:] #可以拷贝列表  把list1拷贝到list2


'''元组'''
# temp = 1
# print(temp)
# print(type(temp))  #输出元素类型  这里是一个int型
# temp2 =[]
# print(type(temp2))  #这里是个空列表
# temp3 = ()
# print(type(temp3)) #这里是个空元组
# temp4 = (1,)
# print(temp4)
# print(type(temp4))#这里是个元组
# print(8*(8))     #直接做一个乘法运算   得64
# print(8*(8,))    #这里定义一个元组然后元组的元素输出8次  (8,8,8,8,8,8,8)
# temp5 = ('asd','dsa','ddd','rrr')
# temp5 = temp5[:2] + ('hhh',) + temp5[2:]   #往元组中插入一个数据,先把元组两边拆开,然后放入元素
# print(temp5)
# del temp5          #删除元组  一般不用,可以自动回收
