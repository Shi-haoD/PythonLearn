class Mystuff(object):
	def __init__(self):#这里自动new了对象执行__new__方法
		self.tangerine = "and now a thound years betwwn"#传递参数赋值
	def apple(self):
		print("i ' am classy apples!")

thing = Mystuff()#new对象
thing.apple()#调用对象的方法
print(thing.tangerine)#调用对象的参数

print("\n"+"*"*10+"\n")
class Song(object):
	def __init__(self,lyrics):#先把下面实例的对象存入lyrics中 ([列表list])
		self.lyrics = lyrics

	def sing_me_song(self):
		for line in self.lyrics:#循环遍历lyrics  ,输出每一行
			print(line)

happy_bady = Song(["Happy birthday to you ",
				   "I don't want to get sued",
				   "So I'll stop right there"])
bulls_on_parade = Song(["they rally around the family ",
						"With pockets full of shells"])
happy_bady.sing_me_song()#先存入再执行

bulls_on_parade.sing_me_song()