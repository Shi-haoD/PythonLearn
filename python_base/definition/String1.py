

'''字符串'''
print ("我叫 %s 今年 %d 岁!" % ('帅哥', 10))#字符串格式化
str1 = 'aaa'
str2 = 'sfaaasss'
'''大小写转换'''
print('第一个字母转换大写',str1.capitalize())   #字符串第一个字母转成大写
print('所有字母转换小写',str2.casefold())       #把字符串所有字符改成小写
print('大写转小写',str2.lower())                #把字符串中的大写字符变成小写
print('小写转大写',str2.upper())                #字符串中小写转成大写
'''次数查找'''

print('指定判断是否是开始的字符',str2.startswith('f',1,2))
#字符串是否是指定开头   s   从什么开始  0   到什么结束  5

print('查找出现次数',str2.count('s'))
#查找在字符串str2中 str1出现的次数
#可以在count(str1,0,10)中添加索引开始和结束

print('是否存在',str2.find('f',0,10))
#检查字符串str1是否在str2中,返回第一次出现位置,没有返回-1

print(str2.rfind(str1,0,10))#和find类似  从右往左
print('会抛出异常的find',str2.index(str1,0,20))
#和find一样,不过如果不在字符串中会抛出一个异常
print(str2.rindex(str1,0,10))#和index方法类似  从右到左


'''字符集判断和查找'''
print('类型判断,数字或者字母',str2.isalnum())
#如果字符串至少有一个字符并且所有字符都是字母或数字则
# 返 回 True,否则返回 False(相同类型)

print('所有字符都是字母',str2.isalpha())
#如果字符串至少有一个字符并且所有字符都是字母则
# 返回 True, 否则返回 False

print('只有数字','12312'.isdigit())
#如果字符串只包含数字则返回 True 否则返回 False.
print('都是小写',str2.islower())
#如果字符串中包含至少一个区分大小写的字符，
# 并且所有这些(区分大小写的)字符都是小写，

'''字符串分割填充'''
print('指定字符分割')
print(','.join(str2))
#用指定字符串分割字符串,前面的时分割符,
# 则返回 True，否则返回 False
#  后面的是被分割的字符串
print('字符串长度',len(str2))            #字符串长度
print('字符串左对齐然后填充',str2.ljust(10,'a'))
#前面是需要修改的字符串,后面是填充的东西
#使用这个方法先将字符串左对齐
#后面的(10)需要添加的字符串数量,后面的('a')是添加的字符
print('右对齐填充',str2.rjust(10,'a'))   #这个是右对其,添加10个'a'

print('截取指定字符或者空格',str.lstrip('sfaaass'))#截取字符串左边的空格或左边指定的字符
print('截取两边的字符或空格',str2.strip())
print('字符串中最大的',max(str2))            #返回字符串中最大的字符
print('字符串中最小的',min(str2 ))           #返回字符串中最小的字符

print('指定字符串内容交换',str2.replace('s','b',10))
#把字符串str2中的's',转换成'b',最多转换10次

print('指定内容作为字符串的分割符',str2.split())
#把a当成分隔符分割字符串  (一般用在字符串中有空格的时候)


print(type(str2))
print(ord('a'))
