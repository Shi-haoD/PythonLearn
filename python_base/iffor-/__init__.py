from sys import  exit

def gold_room():
	print("this is room is full of gold .how much do you take这个房间里装满了金子，你要多少钱？ ")
	choice = input('输入金额')
	if '0' in choice or '1' in choice:
		how_much = int(choice)
	else:
		dead('man , learn totype a number伙计，学会打一个数字')
	if how_much<50:
		print("nice you're not greedy , you win? 你不贪心，你赢了？")
		exit(0)
	else:
		dead("you greedy bastard你贪婪的混蛋")

def bear_room():
	print("there is a bear here这里有一只熊")
	print("the bear has a bunch of honey这只熊有一堆蜂蜜")
	print("the fat bear is in front of another door 那只胖熊站在另一扇门前")
	print("how are you going to move the bear你要怎么搬动那只熊")
	bear_moved = False

	while True:
		choice = input('打蜂蜜或者嘲讽熊 之后可以打开门')
		if choice == '打蜂蜜':
			dead('the bear looks at you then slaps your face off熊看着你然后把你的脸往下掉')
		elif choice == '嘲讽熊' and not bear_moved:
			print('the bear has moved from the door 熊已经从门上移动了')
			print('you can go through it now你现在可以通过它了')
			bear_moved = True
		elif choice == '嘲讽熊' and bear_moved:
			dead('the bear gets pissed off and chews your leg off熊被激怒了，把你的腿咬掉了')
		elif choice == '打开门' and bear_moved:
			gold_room()
		else:
			print('i got no idea what that means我不知道那是什么意思')

def cthulhu_room():
	print("here you see the great evil cthulhu 在这里你可以看到巨大的邪恶的cthulhu")
	print("he , it ,whatever stares at you and you go insane他，不管你怎么盯着你，你都疯了")
	print("do you flee for yout life or eaat your head?你是为了你的生命而逃亡还是在你的脑海中")
	choice = input( '命或者头')
	if '命' in choice:
		start()
	elif '头' in choice:
		dead('we ll taht was tasty我们会很好吃的')
	else:
		cthulhu_room()
def dead(why):
	print(why,'good job')
	exit(0)
def start():
	print('you are in a dark room你在一个黑暗的房间里')
	print('there is a door to your right and left 你的右手 左手边有一扇门')
	print('which one do you take你选哪一个')

	choice = input("左右")
	if choice == '左':
		bear_room()
	elif choice == '右':
		cthulhu_room()
	else:
		dead('your stumble aroumd the rooom untill you starve你的小绊脚，直到你饿死')

start()