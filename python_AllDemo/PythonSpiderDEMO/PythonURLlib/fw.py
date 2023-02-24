import random


def save_data(data):
	with open("shuziz.txt", "a+", encoding='UTF-8') as fp:
		# json.dump(data, fp, ensure_ascii=False, indent=4)
		fp.writelines(data + "\n")


def shengcheng1(num):
	for i in range(num):
		sui1 = random.randint(1, 15)
		sui2 = random.randint(1, 9999999)
		str = "{} {}";
		suiji2 = str.format(sui1, sui2)
		print(suiji2)
		save_data(suiji2)

if __name__ == '__main__':
	shengcheng1(100000000)
